message = 'This is a string.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)
