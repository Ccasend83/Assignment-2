def find_lines_containing(filename, keyword):
    """
    Returns a list of (line_number, line_text) for lines that contain
    keyword (case-insensitive). Line numbers start at 1.
    """
    line_number = 1
    results = []
    # Convert keyword to lowercase once to ensure case-insensitive matching
    keyword_lowercase = keyword.lower()

    # Open the file and iterate through it
    file = open(filename, 'r', encoding='utf-8')

    #
    for line_text in file:
        # Check if the keyword exists in the line (case-insensitive)
        if keyword_lowercase in line_text.lower():
            results.append((line_number, line_text.strip()))

        # Increment the counter for the next line
        line_number += 1

    file.close()
    return results



filename_for_testing = "sample-file.txt"
keyword_for_testing = "data"

# Store the list of tuples (line_number, line_text)
matches = find_lines_containing(filename_for_testing, keyword_for_testing)

# print how many matching lines were found
print(f"Total matching lines found for keyword --> {keyword_for_testing}: {len(matches)}")

# Print the first 3 matching lines
print("First 3 matching lines:")
for line_no, text in matches[:3]:
    print(f"Line {line_no}: {text}")