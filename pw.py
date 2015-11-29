#!/usr/bin/python

# Use the pyperclip module to copy and paste to and from
# the clipboard to create an (INSECURE!) password locker

import pyperclip, sys

# create a dictionary containing account names and passwords

passwords = {
    'email': 'emailpw',
    'blog': 'blogpw',
    'luggage': '12345'
    }

# Make sure that two arguments are passed and give usage info if not

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

# Set account variable to second sys.argv argument

account = sys.argv[1]

# Check to see if account is in the passwords dictionary
# Copy value to clipboard if yes, print error if not

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)


