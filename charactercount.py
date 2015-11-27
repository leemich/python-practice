message= 'Hello.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    charlist = list(count.keys())
print(charlist, sep='/')
