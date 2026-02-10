import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'MyDataScienceProject2 (lucasjoffre@hotmail.com)'
}

list_of_banned_words = ["References", "External links", "See also", "Notes"]
headings_that_are_being_saved = []

# pass the headers into the request
response = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=headers)

soup = BeautifulSoup(response.content, 'html5lib')
main_content = soup.find('div', id='mw-content-text')

for headers in main_content.find_all('h2'):
    text = headers.text
    if text not in list_of_banned_words:
        headings_that_are_being_saved.append(text)

with open('Headings.txt', 'w') as file:
    for heading in headings_that_are_being_saved:
        file.write(heading + '\n')
