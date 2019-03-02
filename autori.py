list_names = list(map(str, input().split("-")))  # split by "-"
short_variation = list(map(lambda name: name[0], list_names))  # get first letter(s) from list of names
output = ''.join(short_variation)  # convert list to string
print(output)
