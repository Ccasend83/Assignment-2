import requests
from bs4 import BeautifulSoup
import csv

# wikipedia has a weird bot policy so we must have a user to access the website
# this is literally just makings the variable headers and passing it into our request.get code
headers = {
    'User-Agent': 'MyDataScienceProject2 (lucasjoffre@hotmail.com)'
}
machine_learning_page_html = requests.get("https://en.wikipedia.org/wiki/Machine_learning",headers=headers)
parsed_machine_learning_page_content = BeautifulSoup(machine_learning_page_html.content, 'html.parser')

# locate the specific content area
main_filtered_content_div = parsed_machine_learning_page_content.find('div', id='mw-content-text')

# find the first table with at least 3 rows
target_table_for_saving = None
for specific_table_found in main_filtered_content_div.find_all('table'):
    if len(specific_table_found.find_all('tr')) >= 3:
        target_table_for_saving = specific_table_found
        break

all_recorded_rows_list = []
maximum_columns = 0

# first pass in and extract everything and find the maximum width
for tr in target_table_for_saving.find_all('tr'):
    # Check for both header (th) and data (td) tags
    raw_wiki_table_cells = tr.find_all(['th', 'td'])
    # separator=' ' ensures "Machine learninganddata mining" becomes "Machine learning and data mining"
    filtered_row_data = [specific_raw_wiki_table_cell.get_text(separator=' ', strip=True) for specific_raw_wiki_table_cell in raw_wiki_table_cells]

    # if line 29 went smoothly this if statement would count as true
    # meaning it will append the data to all_recorded_rows_list
    if filtered_row_data:
        all_recorded_rows_list.append(filtered_row_data)
        if len(filtered_row_data) > maximum_columns:
            maximum_columns = len(filtered_row_data)

# extract headers from <th>; otherwise create col1, col2, etc
# check if the table actually HAS any <th> tags at all to decide our header row
has_any_headers = target_table_for_saving.find('th') is not None

if has_any_headers:
    # use the first row that contains <th> as our header row
    headers = all_data_to_write = []
    header_found = False

    # for each row in our all_recorded_rows_list variable if a header is found it
    # treats it like a title for that first row in the csv
    # we do this so only grab the first row as the header and treat everything else as data
    for specific_row_in_recorded_list in all_recorded_rows_list:
        if not header_found:
            headers = specific_row_in_recorded_list
            header_found = True
        else:
            all_data_to_write.append(specific_row_in_recorded_list)
else:
    # No <th> tags found at all? Create col1, col2, etc.
    headers = [f"col{i + 1}" for i in range(maximum_columns)]
    all_data_to_write = all_rows_list

# pad the file and save using with so we don't have to close our file later
with open('wiki_table.csv', 'w', newline='', encoding='utf-8') as file_writer:
    writer = csv.writer(file_writer)

    # Write the header row and pad when neccessary
    padded_headers_for_file = headers + [""] * (maximum_columns - len(headers))
    writer.writerow(padded_headers_for_file)

    # write the data rows
    for row in all_data_to_write:
        # Pad missing values with empty strings
        padded_row = row + [""] * (maximum_columns - len(row))
        writer.writerow(padded_row)
