#!/usr/bin/python

# wpbullet.py - add Wikipedia-style bullet points to the start of each
# line on the clipboard

import pyperclip

text = pyperclip.paste()

# Separate lines and add asterisks

lines = text.split('\\n')
print(lines)
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\\n'.join(lines)
pyperclip.copy(text)

