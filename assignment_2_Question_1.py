# read the file
file_opener_for_reading = open('sample-file.txt', 'r', encoding='utf-8')
content = file_opener_for_reading.read()


# split into initial tokens
raw_words_from_text_file = content.split()
regular_characters_for_cleaning = "abcdefghijklmnopqrstuvwxyz"
total_word_counts = {}

for individual_words_in_file in raw_words_from_text_file:
    # convert to lowercase
    individual_words_in_file = individual_words_in_file.lower()

    # remove punctuation from beginning and end
    individual_words_in_file = individual_words_in_file.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

    # count alphabetic characters to ensure at least two
    regular_characters_for_counting = 0
    for characters_found_in_each_word in individual_words_in_file:
        if characters_found_in_each_word in regular_characters_for_cleaning:
            regular_characters_for_counting += 1

    if regular_characters_for_counting >= 2:
        # 5. Update frequency count
        if individual_words_in_file in total_word_counts:
            total_word_counts[individual_words_in_file] += 1
        else:
            total_word_counts[individual_words_in_file] = 1

# Sort by count (descending)
# .items() gives a list of words and their counts
# make sure reverse = True so it goes in descending order
final_sorted_words = sorted(total_word_counts.items(), key=lambda x: x[1], reverse=True)

# Print the top 10 in the "word -> count" format
for i in range(min(10, len(final_sorted_words))):
    total_words, total_count = final_sorted_words[i]
    print(f"{total_words} -> {total_count}")
file_opener_for_reading.close()