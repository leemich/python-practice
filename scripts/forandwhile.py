# For loops

a = 0

for i in range(10):
    a += 1
print(a)

a = 0

for i in range(10):
    a += 1
for j in range(10):
    a += 1
print(a)

a = 0
for i in range(10):
    a += 1
    for j in range(10):
        a += 1

print(a)


i = 10
while i > 0:
    print(i)
    i -= 1
