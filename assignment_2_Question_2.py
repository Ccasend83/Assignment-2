# 1. Read the file
f = open('sample-file.txt', 'r', encoding='utf-8')
content = f.read()

# Initial split and cleaning variables
raw_tokens = content.split()
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
alpha_chars = "abcdefghijklmnopqrstuvwxyz"
cleaned_words = []

# 2, 3, & 4. Lowercase, Strip Punctuation, and Filter (min 2 alpha chars)
for token in raw_tokens:
    token = token.lower().strip(punctuation)

    alpha_count = 0
    for char in token:
        if char in alpha_chars:
            alpha_count += 1

    if alpha_count >= 2:
        cleaned_words.append(token)

# 5. Construct Bigrams (pairs of consecutive cleaned words)
bigram_counts = {}
# Use range to len - 1 so the last word doesn't try to pair with a non-existent next word
for i in range(len(cleaned_words) - 1):
    word1 = cleaned_words[i]
    word2 = cleaned_words[i + 1]
    bigram = word1 + " " + word2

    # 6. Count the frequency of each bigram
    if bigram in bigram_counts:
        bigram_counts[bigram] += 1
    else:
        bigram_counts[bigram] = 1

# 7. Sort bigrams by frequency in descending order
sorted_bigrams = sorted(bigram_counts.items(), key=lambda x: x[1], reverse=True)

# Print the top 5
for i in range(min(5, len(sorted_bigrams))):
    pair, count = sorted_bigrams[i]
    print(f"{pair} -> {count}")
f.close()