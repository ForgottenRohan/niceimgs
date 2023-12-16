import requests
from bs4 import BeautifulSoup
import os
import transliterate



def get_links(url):
    response = requests.get(
        url=url,
    )
    soup = BeautifulSoup(response.text, 'lxml')
    imgs = soup.find_all('img', itemprop='thumbnail')
    count, links = 1, []
    amount = len(imgs) + 1
    for img in imgs:
        link = img.get('src')
        links.append(link)
        count += 1
    return links

def translate(tag:str):
    tagg = transliterate.translit(tag, reversed=True)
    end_tagg = tagg.lower()
    end_tag = end_tagg.replace(' ', '')
    return end_tag
    
def main(tag:str):
    end_tag = translate(tag)
    try:
        links = get_links(f'https://ru.wallpaper.mob.org/pc/gallery/tag={end_tag}/')
        return links
    except Exception as _ex:
        return _ex

if __name__ == '__main__':
    main('Anime')
    