def find_lines_containing_specific_word(inserted_filename_for_checking, inserted_keyword_for_checking):

    #returns a list of initial_line_number, line_text for lines that contain
    #inserted_keyword_for_checking (case-insensitive). Line numbers start at 1.

    initial_line_number = 1
    final_sorted_results = []
    # convert keyword to lowercase once to ensure case-insensitive matching
    keyword_for_testing_lowercase = inserted_keyword_for_checking.lower()

    # open the file and iterate through it
    inserted_file_for_reading = open(inserted_filename_for_checking, 'r', encoding='utf-8')

    # for loop outputs each individual line found in inserted_file_for_reading
    for text_for_each_line in inserted_file_for_reading:
        # check if the keyword exists in the line (case-insensitive)
        if keyword_for_testing_lowercase in text_for_each_line.lower():
            final_sorted_results.append((initial_line_number, text_for_each_line.strip()))

        # Increment the counter for the next line
        initial_line_number += 1

    # return our final results and close the file
    inserted_file_for_reading.close()
    return final_sorted_results


# example cases
filename_for_testing = "sample-file.txt"
keyword_for_testing = "data"

# stores the total matches found using keyword_for_testing
total_matches_found = find_lines_containing_specific_word(filename_for_testing, keyword_for_testing)

# prints how many matching lines were found
print(f"Total matching lines found for keyword --> {keyword_for_testing}: {len(total_matches_found)}")

# prints the first 3 matching lines
print("First 3 matching lines:")
for line_number, follow_up_text in total_matches_found[:3]:
    print(f"Line {line_number}: {follow_up_text}")