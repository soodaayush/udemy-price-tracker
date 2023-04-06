import requests
from bs4 import BeautifulSoup
import lxml


def scrapeUdemy(tag):
    url = f'https://www.udemy.com/courses/search/?src=ukw&q={tag}'
    response = requests.get(url)

    h3s = []

    soup = BeautifulSoup(response.text, 'html.parser')

    # title = soup.select('.ud-heading-md')[0].getText().strip()
    # print(soup.title)

    a = soup.find('a', attrs={'class': 'class'})

    for tags in soup.find_all('a'):
        # print(tags.get('href'))
        h3s.append(tags.get('href'))

    return response.text


courseTag = input("Search for Udemy courses?")
print(scrapeUdemy(courseTag))
