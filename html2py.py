from bs4 import BeautifulSoup


def html2text(html):
    soup = BeautifulSoup(html)
    text_parts = soup.findAll(text=True)
    return ''.join(text_parts)
