#!/usr/bin/python
# Script for a homemade quiz that tracks score

# Set base score and base number correct
score = 0
number_correct = 0

# First question

first = int(input("How many dimes in a dollar? Please answer with a number only. "))

if first == 10:
    print("Correct!")
    score = 10
    number_correct += 1
else:
    print("I'm sorry. That is incorrect.")

print()
print("Your current score is ", score)
print()

# Second Question

answer_two = "mommy"

answer_two_input = input("Who did I see kissing Santa Claus underneath the mistletoe last night? ")

if answer_two_input.lower() == answer_two:
    print("Correct!")
    score += 10
    number_correct += 1
else:
    print("I'm sorry. That is incorrect.")

print()
print("Your current score is ", score)
print()

# Third question

year = int(input("How many days are there in a year? Please answer with a number only. "))

if year == 365:
    print("Correct!")
    score += 10
    number_correct += 1
else:
    print("I'm sorry. That is incorrect.")

print()
print("Your current score is ", score)
print()

# Fourth Question

month = input("What is the third month of the year? ")

if month.lower() == "march":
    print("Correct!")
    score += 10
    number_correct += 1
else:
    print("I'm sorry. That is incorrect.")

print()
print("Your current score is ", score)
print()

# Fifth question

ques = int(input("This is the last question. How many questions were on this quiz? "))

if ques == 5:
    print("Correct!")
    score += 10
    number_correct += 1
else:
    print("I'm sorry. That is incorrect.")

percentage_correct = (number_correct / 5) * 100

print()
print("Your final score is ", score)
print("You got", percentage_correct, "% of the questions correct.")
print()



    




    




