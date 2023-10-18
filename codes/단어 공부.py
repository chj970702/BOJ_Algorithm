word = input()
upword = word.upper()

unique = set(upword)
dict = {}
for item in unique:
    dict[item] = upword.count(item)
max_count = max(dict.values())

value = list(dict.values())
if value.count(max(value)) > 1:
    print("?")
else:
    idx = value.index(max(value))
    print(list(dict.keys())[idx])