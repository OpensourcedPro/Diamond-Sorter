  # Insert the broken down URL parts into the url_domains table
import logging
from urllib.parse import urljoin, urlparse
from multiprocessing.dummy import Pool as ThreadPool
import requests
from requests.adapters import HTTPAdapter, Retry
from bs4 import BeautifulSoup
import argparse
import sqlite3

logging.basicConfig(
    format='%(message)s',
    level=logging.INFO)


def fetch_html_content(url: str):
    request = requests.Session()
    retries = Retry(total=2, backoff_factor=1)
    request.mount('https://', HTTPAdapter(max_retries=retries))
    try:
        response = request.get(url, timeout=1)
        return response.text
    except requests.exceptions.HTTPError as errh:
        logging.exception(f"The {url} has Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        logging.exception(f"The {url} has Error Connecting Problem:", errc)
    except requests.exceptions.Timeout as errt:
        logging.exception(f"The {url} has Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        logging.exception(f"The url {url} has Something Else:", err)
    return None


def get_linked_urls(url: str, html: str):
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        path = link.get('href')
        if path and path.startswith('/'):
            path = urljoin(url, path)
        yield path


class Crawler:
    def __init__(self, url: str, db_path: str):
        self.entrypoint = url
        self.visited_urls = set()
        self.urls_queue = [self.entrypoint]
        self.db_path = db_path

        # Create the url_domains table if it doesn't exist
        self.create_url_domains_table()

    def create_url_domains_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS url_domains (
            base_url TEXT,
            base_path TEXT,
            relative_path TEXT,
            relative_url TEXT,
            script_path TEXT,
            path_info TEXT
        )
        """
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def validate_url(self, url: str) -> bool:
        return url and url.startswith("http") and url.startswith(self.entrypoint)

    def add_url_to_queue(self, url: str) -> None:
        if url not in self.visited_urls and url not in self.urls_queue and self.validate_url(url):
            self.urls_queue.append(url)

    def crawl(self, url: str) -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("BEGIN TRANSACTION")

            self.visited_urls.add(url)
            html = fetch_html_content(url)
            if html:
                page_content_urls = set()
                for page_url in get_linked_urls(url, html):
                    self.add_url_to_queue(page_url)
                    page_content_urls.add(page_url)
                urls = [url for url in page_content_urls if url and url.startswith("http")]
                logging.info(f"Current page: {url}")
                logging.info("The connected URLs in the page:")
                for url in urls:
                    parsed_url = urlparse(url)
                    base_url = parsed_url.scheme + "://" + parsed_url.netloc
                    relative_path = parsed_url.path
                    relative_url = parsed_url.geturl()
                    script_path = parsed_url.path.rsplit("/", 1)[0]
                    path_info = parsed_url.path.split("/")[-1]
                    logging.info(f"    Base URL: {base_url}")
                    logging.info(f"    Base Path: {relative_path}")
                    logging.info(f"    Relative Path: {relative_url}")
                    logging.info(f"    Script Path: {script_path}")
                    logging.info(f"    Path Info: {path_info}")

                    insert_query = "INSERT INTO url_domains (base_url, base_path, relative_path, relative_url, script_path, path_info) VALUES (?, ?, ?, ?, ?, ?)"
                    cursor.execute(insert_query, (base_url, relative_path, relative_path, relative_url, script_path, path_info))

                conn.commit()

        except Exception as e:
            logging.exception(f"An error occurred while crawling {url}: {e}")

        finally:
            cursor.close()
            conn.close()

    def run(self) -> None:
        while self.urls_queue:
            pool = ThreadPool(3)
            pool.map(self.crawl, self.urls_queue)
            self.urls_queue.pop(0)
            pool.close()
            pool.join()

    def cleanup(self):
        self.conn.close()


def args_helper():
    parser = argparse.ArgumentParser()
    parser.add_argument('entrypoint')
    parser.add_argument('--db-path', default='cookie_data.db')
    return parser.parse_args()


if __name__ == '__main__':
    config = args_helper()
    entrypoint = config.entrypoint
    db_path = config.db_path
    if entrypoint:
        crawler = Crawler(entrypoint, db_path)
        try:
            crawler.run()
        finally:
            crawler.cleanup()