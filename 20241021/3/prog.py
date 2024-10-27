from collections import Counter

W = int(input())

text_i = []
while (line := input()):
    if line.strip() == "":
        break
    text_i.append(line)

text = " ".join(text_i)

clean = []
for c in text:
    if c.isalpha() or c.isspace():
        clean.append(c.lower())
    else:
        clean.append(' ')

clean = ''.join(clean)
words = clean.split()
word_counts = Counter(word for word in words if len(word) == W)

if not word_counts:
    exit()
max_fr = max(word_counts.values())

most_common = sorted(word for word, count in word_counts.items() if count == max_fr)

print(" ".join(most_common))

import sys
exec(sys.stdin.read())
