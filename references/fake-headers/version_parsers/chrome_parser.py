# Or use my header parser:
# https://raw.githubusercontent.com/TheDevFromKer/Headers-Parser

from bs4 import BeautifulSoup
from requests import Session


URL = 'https://en.wikipedia.org/wiki/Google_Chrome_version_history'


def get_text() -> str:
    with Session() as s:
        text = s.get(URL).text

    return text


def parse_versions(html: str) -> list:
    versions = []
    bs = BeautifulSoup(html, 'html5lib')

    table = bs.find('table', {'style': 'font-size:95%;'})
    body = table.find('tbody')
    rows = body.findAll('tr')

    for row in rows:
        try:
            ver = row.find('td').text
            versions.append(ver.strip())
        except Exception:
            pass

    return [*reversed(versions)]


print(parse_versions(get_text()))
