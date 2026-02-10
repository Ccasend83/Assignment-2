import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {
    'User-Agent': 'MyDataScienceProject2 (lucasjoffre@hotmail.com)'
}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Locate the specific content area
content_div = soup.find('div', id='mw-content-text')

# Find the first table with at least 3 rows
target_table = None
for table in content_div.find_all('table'):
    if len(table.find_all('tr')) >= 3:
        target_table = table
        break

all_rows = []
max_cols = 0

# 1. First pass: Extract everything and find the maximum width
for tr in target_table.find_all('tr'):
    # Check for both header (th) and data (td) tags
    cells = tr.find_all(['th', 'td'])
    # separator=' ' ensures "Machine learninganddata mining" becomes "Machine learning and data mining"
    row_data = [cell.get_text(separator=' ', strip=True) for cell in cells]

    if row_data:
        all_rows.append(row_data)
        if len(row_data) > max_cols:
            max_cols = len(row_data)

# 2. Header Logic:
# The prompt asks to extract headers from <th>; otherwise create col1, col2...
# We check if the table actually HAS any <th> tags at all to decide our header row
has_any_headers = target_table.find('th') is not None

if has_any_headers:
    # Use the first row that contains <th> as our header row
    headers = all_data_to_write = []
    header_found = False
    for row in all_rows:
        if not header_found:
            headers = row
            header_found = True
        else:
            all_data_to_write.append(row)
else:
    # No <th> tags found at all? Create col1, col2, etc.
    headers = [f"col{i + 1}" for i in range(max_cols)]
    all_data_to_write = all_rows

# 3. Final Step: Pad and Save
with open('wiki_table.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # Write the header row (padded if necessary)
    padded_headers = headers + [""] * (max_cols - len(headers))
    writer.writerow(padded_headers)

    # Write the data rows
    for row in all_data_to_write:
        # Pad missing values with empty strings
        padded_row = row + [""] * (max_cols - len(row))
        writer.writerow(padded_row)

print(f"File saved. Detected {max_cols} columns.")