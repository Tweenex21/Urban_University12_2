def all_variants(text):
    length = len(text) + 1
    for i in range(1, length):
        for j in range(length - i):
            yield text[j: j + i]


a = all_variants("abc")
for i in a:
    print(i)