def count_text(text):
    pairs = set()
    text = text.lower()
    for i in range(len(text) -1):
        if text[i].isalpha() and text[i+1].isalpha():
            p = text[i] + text[i+1]
            pairs.add(p)
    return len(pairs)

text = input()
print(count_text(text))

import sys
exec(sys.stdin.read())
