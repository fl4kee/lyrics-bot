import requests
import lxml.html
from lxml import etree

artist, song = input().lower().replace(' ','').split('-')

r = requests.get(f'https://www.azlyrics.com/lyrics/{artist}/{song}.html')

if r.status_code == 200:
    tree = lxml.html.document_fromstring(r.text)
    text = tree.xpath('/html/body/div[2]/div/div[2]/div[5]/text()')
    lyrics = ''
    for i in text:
        lyrics += i
    print(lyrics)