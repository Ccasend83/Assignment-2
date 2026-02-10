# read the file
f = open('sample-file.txt', 'r', encoding='utf-8')
content = f.read()


# split into initial tokens
raw_tokens = content.split()

punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
alpha_chars = "abcdefghijklmnopqrstuvwxyz"
word_counts = {}

for token in raw_tokens:
    # 2. Convert to lowercase
    token = token.lower()

    # 3. Remove punctuation from beginning and end
    token = token.strip(punctuation)

    # 4. Count alphabetic characters to ensure at least two
    alpha_count = 0
    for char in token:
        if char in alpha_chars:
            alpha_count += 1

    if alpha_count >= 2:
        # 5. Update frequency count
        if token in word_counts:
            word_counts[token] += 1
        else:
            word_counts[token] = 1

# Sort by count (descending)
# .items() gives a list of (word, count) tuples
sorted_items = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Print the top 10 in the "word -> count" format
for i in range(min(10, len(sorted_items))):
    word, count = sorted_items[i]
    print(f"{word} -> {count}")
f.close()