from bs4 import BeautifulSoup
from requests import Session


def get_text() -> str:
    with Session() as s:
        text = s.get('https://www.mozilla.org/en-US/firefox/releases/').text

    return text


def parse_versions(html: str) -> list:
    versions = []
    bs = BeautifulSoup(html, 'html5lib')

    main = bs.find('main', {'id': 'main-content'})
    table = main.find('ol', {'class': 'c-release-list'})
    rows = table.findAll('li')

    for row in rows:
        try:
            first = row.find('strong')
            second = first.find('a').text
            versions.append(second)

            first = row.find('ol')
            second = first.findAll('li')

            for item in second:
                a = item.find('a').text
                versions.append(a)

        except Exception:
            pass

    return versions


print(parse_versions(get_text()))
