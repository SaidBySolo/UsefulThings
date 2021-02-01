from bs4 import BeautifulSoup


def html2text(html):
    soup = BeautifulSoup(html, 'html.parser')
    text_parts = soup.findAll(text=True)
    return ''.join(text_parts)
