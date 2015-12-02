#!/usr/bin/python
#
# Coding challenge #2 - Magic 8 Ball

import random, time

answers = [
    'It is certain',
    'It is decidely so',
    'Without a doubt',
    'Yes, definitely',
    'You may rely on it',
    'As I see it, yes',
    'Most likely',
    'Outlook good',
    'Yes',
    'Signs point to yes',
    'Reply hazy; try again',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    'Don\'t count on it',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful']


while True:
    print('Ask your question, and the Magic 8 Ball will give you an answer. Press \'Q\' to quit')

    question = input()
    
    if question.upper() == 'Q':
        break
    
    print()
    print('One moment, please. The Magic 8 Ball is thinking . . .')
    print()
    
    time.sleep(5)
    
    print('You asked: ' + question)
    print()

    answer_picked = random.choice(answers)
    print(answer_picked)
    print()

