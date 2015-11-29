# Examples of justified and centered text

print('''

LEFT AND RIGHT JUSTIFIED TEXT
------------------------------

The 1st argument passed to the ljust() or rjust() methods
is the total length of the string to be printed.

A string 5 chars long with .rjust(10) called on it
will move the string to the right with 5 whitespace chars
to the left of it in a string with a total of 10 chars.

For example, the following code:

spam = 'Hello'

print(spam.rjust(10))
print(spam.rjust(20))
print(spam.ljust(15))

will print:

''')

spam = 'Hello'

print(spam.rjust(10))
print(spam.rjust(20))
print(spam.ljust(15))
print()
print('----------------------------------')
print()


print('''A second argument can be passed to fill the space with a
char other than white space. Examples:

print(spam.rjust(10, '.'))
print(spam.rjust(20, '*'))
print(spam.ljust(15, '~'))

This prints:

''')

print(spam.rjust(10, '.'))
print(spam.rjust(20, '*'))
print(spam.ljust(15, '~'))
print()
print()
print('''
CENTERING TEXT
---------------

The center() method works just like the ljust() and rjust()
methods, except it (surprise!) centers the text.

For example, the following code:

print(spam.center(20))
print()
print(spam.center(20, '.'))

returns the following:

''')

print(spam.center(20))
print()
print(spam.center(20, '.'))
print()

print('''As you can see, the center() method can also take a
second argument which designates the character to be used to
fill the space.

--------------------------------------------

USING JUSTIFY TO PRINT TABULAR DATA

You can use justified text to neatly print data in a table.

For example:

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth, '.'))
        
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

printPicnic(picnicItems, 12, 5)
print()
printPicnic(picnicItems, 20, 6)

This is what the code looks like when it's executed:


''')

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth, '.'))
        
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

printPicnic(picnicItems, 12, 5)
print()
printPicnic(picnicItems, 20, 6)
      


