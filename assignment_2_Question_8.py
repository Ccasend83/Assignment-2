import requests
from bs4 import BeautifulSoup

# wikipedia has a weird bot policy so we must have a user to access the website
# this is literally just makings the variable headers and passing it into our request.get code
headers = {
    'User-Agent': 'MyDataScienceProject2 (lucasjoffre@hotmail.com)'
}

list_of_banned_words = ["References", "External links", "See also", "Notes"]
headings_that_are_being_saved = []

# pass the headers into the request
data_science_page_html = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=headers)

# convert data_science_page_html into readable content that we can go through
# use .find to select the correct body text
parsed_data_science_page_content = BeautifulSoup(data_science_page_html.content, 'html.parser')
main_filtered_content = parsed_data_science_page_content.find('div', id='mw-content-text')

# for loop stores each individual header found in the page and converts it to found_headers_in_page
for individual_headers_in_page in main_filtered_content.find_all('h2'):
    found_headers_in_page = individual_headers_in_page.text
    # if found_headers_in_page is not in our list of banned words it appends it to a list
    # (headings_that_are_being_saved)

    if found_headers_in_page not in list_of_banned_words:
        headings_that_are_being_saved.append(found_headers_in_page)

# open a file named Headings in write mode using with
with open('Headings.txt', 'w') as file:
    # write the headings found in headings_that_are_being_saved in our file and move to
    for headings_that_are_being_written in headings_that_are_being_saved:
        file.write(headings_that_are_being_written + '\n')
