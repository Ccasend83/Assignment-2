# read the file
file_opener_for_reading = open('sample-file.txt', 'r', encoding='utf-8')
content_of_opened_file = file_opener_for_reading.read()

# initial split and cleaning variables
# split the words into a list
raw_words_from_text_file = content_of_opened_file.split()
regular_characters_for_cleaning = "abcdefghijklmnopqrstuvwxyz"
cleaned_words_from_file = []

# lowercase, remove punctuation, and filter minimum 2 characters to all
for individual_words_in_file in raw_words_from_text_file:
    individual_words_in_file = individual_words_in_file.lower().strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

    character_cleaning_count = 0
    for character_found in individual_words_in_file:
        if character_found in regular_characters_for_cleaning:
            character_cleaning_count += 1

    if character_cleaning_count >= 2:
        cleaned_words_from_file.append(individual_words_in_file)

# construct the Bigrams (pairs of consecutive cleaned words)
bigram_counts_from_cleaned_words = {}
# use range to len - 1 so the last word doesn't try to pair with a non-existent next word
for paired_words_finder in range(len(cleaned_words_from_file) - 1):
    matched_word_1 = cleaned_words_from_file[paired_words_finder]
    matched_word_2 = cleaned_words_from_file[paired_words_finder + 1]
    individual_listed_bigram = matched_word_1 + " " + matched_word_2

    # count the frequency of each bigram
    if individual_listed_bigram in bigram_counts_from_cleaned_words:
        bigram_counts_from_cleaned_words[individual_listed_bigram] += 1
    else:
        bigram_counts_from_cleaned_words[individual_listed_bigram] = 1

# sort bigrams by frequency in descending order
# make sure reverse = True so it goes in descending order
sorted_listed_bigrams = sorted(bigram_counts_from_cleaned_words.items(), key=lambda x: x[1], reverse=True)

# print the top 5
for single_top_five_bigrams in range(min(5, len(sorted_listed_bigrams))):
    specific_found_word_pair, number_of_times_a_word_pair_is_found = sorted_listed_bigrams[single_top_five_bigrams]
    print(f"{specific_found_word_pair} -> {number_of_times_a_word_pair_is_found}")

file_opener_for_reading.close()