import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'https://www.kinoafisha.info/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS)
    return req

@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='movieItem_info')
    movie_film = []
    for item in items:
        movie_film.append(
            {
                'title_url': URL + item.find('a').get('href'),
                'title': item.find('div', class_='movieItem_title').get_text(),
                'image': URL + item.find('div', class_='picture_image').find('img').get('src'),
                'genre': item.find('div',  class_='movieItem_genres')
            }
        )

        return movie_film

    @csrf_exempt
    def parser():
        html = get_html(URL)
        if html.status_code == 200:
            movie_film1 = []
            for page in range(0, 1):
                html = get_html(f'https://kg.kinoafisha.info/movies/', params=page)
                movie_film1.extend(get_data(html.text))
            return movie_film1
                # print(f'\n{movie_film1}')
        else:
            raise Exception('Parse Error......')
    parser()

