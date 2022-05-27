import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

siesvi = open('quiz4.csv', 'w', encoding='utf8', newline='\n')
siesvi_obj = csv.writer(siesvi)
siesvi_obj.writerow(["movie_title", "movie_label", "movie_link"])
index = 1
while index < 6:
    url = "https://animetv.night-city.online/page/" + str(index)
    language = {'Accept-Language': 'en-US'}
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    soup_all = soup.find('div', 'section__content section__items')
    yvela_filmi = soup_all.find_all('div', 'movie-item')
    for each in yvela_filmi:
        movie_title = each.find('div', 'movie-item__meta ws-nowrap').span.text
        movie_label = each.find('div', 'movie-item__label').text
        movie_link = each.find('a', 'movie-item__link').get('href')
        print(movie_link)
        siesvi_obj.writerow([movie_title, movie_label, movie_link])
    index += 1
    sleep(randint(15, 20))

