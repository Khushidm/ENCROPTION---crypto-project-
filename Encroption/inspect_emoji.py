# inspect_emoji.py
s = input("Paste emoji/text here: ")
print("First 40 characters and codepoints:")
for i, ch in enumerate(s[:40]):
    print(i, repr(ch), hex(ord(ch)))
