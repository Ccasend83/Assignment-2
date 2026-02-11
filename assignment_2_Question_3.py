# 1. Read the file
f = open('sample-file.txt', 'r', encoding='utf-8')
lines = f.readlines()


punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
whitespace = ' \t\n\r\x0b\x0c'
near_duplicate_groups = {}

# process each line to create a "normalized" key
for i in range(len(lines)):
    original_line = lines[i].strip('\n')  # Keep original text minus the newline
    line_number = i + 1

    # create the normalized version
    normalized = ""
    for char in original_line:
        char_lower = char.lower()
        # remove whitespace and punctuation
        if char_lower not in punctuation and char_lower not in whitespace:
            normalized += char_lower

    # ignore empty lines after normalization
    if normalized == "":
        continue

    # group lines by their normalized version
    if normalized not in near_duplicate_groups:
        near_duplicate_groups[normalized] = []

    # store as a tuple of (line_number, original_text)
    near_duplicate_groups[normalized].append((line_number, original_line))

# filter for sets that actually have duplicates (more than 1 line)
duplicate_sets = []
for key in near_duplicate_groups:
    if len(near_duplicate_groups[key]) > 1:
        duplicate_sets.append(near_duplicate_groups[key])

#  print the number of such sets
print(f"Number of near-duplicate sets --> {len(duplicate_sets)}")
print("*" * 30)

#  print the first two sets found
for i in range(min(2, len(duplicate_sets))):
    print(f"Set {i + 1}:")
    current_set = duplicate_sets[i]
    for line_num, text in current_set:
        print(f"{line_num}--> {text}")
    print("*" * 30)

f.close()