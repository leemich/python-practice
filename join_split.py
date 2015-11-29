# Examples of the join() and split() string methods
# with explanations

jlist = ['This', 'is', 'a', 'string', 'made', 'from', 'a', 'list', 'of', 'strings.']

print('THE join() METHOD')
print('------------------')
print('This is a list of strings to be joined:')
print()
print(jlist)
print()
print('It is assigned to a variable called \'jlist\'.')
print()
print('''We call the join() method on a string containing a delimeter
(in this case a string containing a space) and pass it the list contained
in the jlist variable:

' '.join(jlist)

And it returns the following:
''')

jstr = ' '.join(jlist)
print(jstr)

print()
print('THE split() METHOD')
print('-------------------')
print()
sstr = 'This is a string that will be split into a list of strings.'
print(sstr)
print()
print('''The above string is assigned to a variable called \'sstr\'.

We use the split method by calling it on a string. Without an argument,
the method splits the string wherever whitespace, newline, or tab
characters are found.''')
print()
print('''To split our variable, we can do the following:

sstr.split()

and assign the returned value to a variable called \'slist\'.

We can then print slist:''')

slist = sstr.split()
print()
print(slist)
print()
print('---------------------------------------')
print()
print('''The split() method takes a delimeter argument.

For example, say our string looked like this:

scolstr = \'This:is:a:string.\'

We can use the split() method on this string by passing a delimeter
argument to it like so:

scolstr.split(\':\')

This will split the string using a colon as the delimeter rather
than the default whitespace, tab, or newline characters.

If we assign the output of our split method to a variable called \'scollist\'
and then print the result, we get:''')

scolstr = 'This:is:a:string.'
scollist = scolstr.split(':')
print()
print(scollist)
print()
print('---------------------------------------')

print()
print('''REMEMBER: The join() method is called on a delimeter string,
takes a list as its argument, and returns a string composed of the strings
in the list it was passed joined by the delimeter string upon which it
was called.

The split() method is called on a string, takes an optional delimeter
as its argument (with whitespace, tabs, and newline characters being the
default delimeter), and returns a list of strings made up of characters
in the original string with the split happening at the delimeter specified
in the argument passed to the method.''')
print()


