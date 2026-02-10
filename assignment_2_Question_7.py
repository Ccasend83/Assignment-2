import requests
from bs4 import BeautifulSoup

# Create a headers dictionary with a User
# It's best practice to include your contact info (like an email) for Wikipedia
headers = {
    'User-Agent': 'MyDataScienceProject2 (lucasjoffre@hotmail.com)'
}

# pass the headers into the request
response = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=headers)

soup = BeautifulSoup(response.content, 'html5lib')

# now you can proceed with the rest of your scraping
print(f"Title: {soup.title.string}")

main_content = soup.find('div', id='mw-content-text')

for paragraph_text in main_content.find_all('p', recursive=True):
    # get text and strip leading/trailing whitespace
    clean_text = paragraph_text.get_text().strip()

    # check if the stripped text meets the 50-character threshold
    if len(clean_text) >= 50:
        print(clean_text)
        break  # stop after finding the first one

