# Examples of the methods used to strip characters from strings

print('''

STRIPPING CHARACTERS FROM STRINGS
----------------------------------

The strip() method is called on a string and returns a string
with whitespace stripped from the beginning and end of the original
string.

The lstrip() and rstrip() methods do the same thing, except they
only remove whitespace from the left and right sides respectively.

Example:

spam = '     Hello, world!     '
print(spam.strip())
print()
print(spam.lstrip())
print()
print(spam.rstrip())

This code returns the following:

''')


spam = '     Hello, world!     '
print(spam.strip())
print()
print(spam.lstrip())
print()
print(spam.rstrip())
print()

print('''
----------------------------------------------

You can also pass an argument to the methods telling them which
chars should be stripped from the string.

For example:

spam = 'aaaThis is a string.aaa'
print(spam.strip('aaa'))
print(spam.lstrip('aaa'))
print(spam.rstrip('aaa'))

This prints:
''')

spam = 'aaaThis is a string.aaa'
print(spam.strip('aaa'))
print(spam.lstrip('aaa'))
print(spam.rstrip('aaa'))

print('''

NOTE: The order of the chars in the string passed as an argument
to the strip(), lstrip(), and rstrip() methods do not matter.

Examples:

spam = 'abcThis is a string.bca'
print(spam.strip('abc'))
print(spam.strip('bca'))
print(spam.strip('cab'))

When the code above is executed, it strips the preceding 'abc'
and trailing 'bca' from the spam string even though the arguments
passed contain the chars in different orders and the chars in the
string are in different orders:

''')

spam = 'abcThis is a string.bca'
print(spam.strip('abc'))
print(spam.strip('bca'))
print(spam.strip('cab'))
print()

