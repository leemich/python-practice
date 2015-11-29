# The Camel Game
# An exercise/lab from programarcadegames.com

# Import the random library so we can use its functions to generate random numbers
import random

# Print the intro message
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and escape the natives.")

# Set intial done value to false in case we need to end the program

done = False

# Set in-game variables
miles_traveled = 0
thirst = 0
camel_tired = 0
natives_trv = -20
drinks_left = 10

# Main game loop

while done == False:
    print()
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit the game.")
    print()
    print("Make your choice: ")
    
    user_choice = input()

    print()

# Check choice and alter variables accordingly
# Check first to see if user would like to quit    
    if user_choice.upper() == "Q":
        done = True
        break

# Check user status
    elif user_choice.upper() == "E":
        print("Miles traveled: " + str(miles_traveled))
        print("Drinks in canteen: " + str(drinks_left))
        print("The natives are " + str(miles_traveled - natives_trv) + " miles behind you.")
        
# Drink from canteen
    elif user_choice.upper() == "A":
        if drinks_left <= 0:
            print("There is no water left in the canteen.")
        else:
            drinks_left -= 1
            thirst = 0
            print("You take a drink from your canteen.")

# If user chooses to move ahead full speed
    elif user_choice.upper() == "C":
        print("You set off on your camel as fast as he can carry you.")
        daily_travel = random.randrange(10, 21)
        miles_traveled += daily_travel
        thirst += 1
        camel_tired += random.randrange(1, 4)
        natives_trv += random.randrange(7, 15)
        
# Add 1-in-20 chance to find an oasis when player is moving.
# Should prob make this a function since I'll have to call  it twice,
# but I haven't learned those well enough yet. Change later?

        oasis_chance = random.randrange(1, 21)
        if oasis_chance == 11:
            print("You have found an oasis!")
            print("You fill your canteen with clear, cool water, and your camel\nis well rested.")
            if thirst > 4:
                print("You are no longer thirsty.")
            thirst = 0
            drinks_left = 10
            camel_tired = 0

        print("After a long, hard day under the hot sun, you have traveled " + str(daily_travel) + " miles.")

# If user chooses to move ahead moderate speed
    elif user_choice.upper() == "B":
        print("You set off on your camel at a moderate pace.")
        daily_travel = random.randrange(5, 11)
        miles_traveled += daily_travel
        thirst += 1
        camel_tired += 1
        natives_trv += random.randrange(2, 8)
        oasis_chance = random.randrange(1, 21)
        if oasis_chance == 11:
            print()
            print("You have found an oasis!")
            print("You fill your canteen with clear, cool water, and your camel\nis well rested.")
            if thirst > 4:
                print("You are no longer thirsty.")
            print()
            thirst = 0
            drinks_left = 10
            camel_tired = 0
        print("After a long, hard day under the hot sun, you have traveled " + str(daily_travel) + " miles.")

# If the user rests for the night        
    elif user_choice.upper() == "D":
        camel_tired = 0
        natives_trv += random.randrange(7, 15)
        if miles_traveled > natives_trv:
            print("The camel is happy and well-rested, but the natives have drawn closer overnight.")

# Check to see if player has traveled 200 miles (win state)

    if miles_traveled >= 200:
        print()
        print("You have won!")
        print("You have successfully crossed the desert with your faithful camel!")
        done = True
        break

# Check to see if natives have caught up
    if natives_trv >= miles_traveled :
        print()
        print("The natives have caught up to you!")
        print("The last thing you see before death overtakes you is a native\n leading your faithful camel away.")
        print("You have been beaten to death by the natives.")
        done = True
        break

# Check for thirst level and camel tiredness
    if thirst > 6:
        print()
        print("You have died of thirst!")
        done = True
        break
    if camel_tired > 8:
        print()
        print("Your camel has died of exhaustion. There is nothing to do now but\n wait for the natives -- and death -- to overtake you.")
        done = True
        break
    if thirst > 4:
        print()
        print("You are thirsty.")
    if camel_tired > 5:
        print()
        print("Your camel is getting tired. You should rest soon.")

# Let the player know how close the natives are
    if miles_traveled - natives_trv < 15:
        print()
        print("The natives are getting close!")


        


        
        
