import requests
from bs4 import BeautifulSoup

# wikipedia has a weird bot policy so we must have a user to access the website
# this is literally just makings the variable headers and passing it into our request.get code
headers = {
    'User-Agent': 'MyDataScienceProject2 (lucasjoffre@hotmail.com)'
}

# pass the headers into the request
data_science_page_html = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=headers)

parsed_data_science_page_content = BeautifulSoup(data_science_page_html.content, 'html.parser')

# print out the title found in the page
print(f"Title: {parsed_data_science_page_content.title.string}")

# port the parsed data into main_filtered_content and search for the correct body using
# the id mw-content-text
main_filtered_content = parsed_data_science_page_content.find('div', id='mw-content-text')

for selected_paragraph_text in main_filtered_content.find_all('p', recursive=True):
    # get text and strip leading and remove trailing whitespace
    clean_text = selected_paragraph_text.get_text().strip()

    # check if the stripped text meets the 50-character threshold
    if len(clean_text) >= 50:
        print(clean_text)
        break  # stop after finding the first paragraph

