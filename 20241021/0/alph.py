import string
s = set(input())
gl = set("aoueiy")
sogl = set(string.ascii_lowercase) - gl
print(len(s & sogl), len(s & gl))
