"""Author :Rawan Khaled """

import sys

Player1_guess=[]
player2_guess=[]
Player1_input=[]
Player2_input=[]

numbers1=[]
numbers2=[]

guess = 0
count = 0
count1=0
count2=0

test=True

def compare_fun(numbers1, numbers2, count, play):
    global  guess
    guess = 0

    if numbers1 == numbers2 and count == 0:
        if play==2:
            print("Player",play,"is Crowned the MasterMind.")
            sys.exit()
    elif numbers1 == numbers2:
        if play==2:
            print("Now it's Player1's turn.")
            return False
        else:
            return False

    for num1, num2 in zip(numbers1, numbers2):
        if num1 == num2:
            print("You guessed", num2, "correct.")
            guess += 1
        count += 1

    if guess == 0:
        print("Sorry, you didn't guess any number correctly.")

    numbers2.clear()
    return True

print("--------Welcome To The MasterMinds Game---------")

player1_input=input("Player1: Enter the number you wish: ")
player1_input.split()

for number in player1_input:
    numbers1.append(int(number))
len1=len(numbers1)
print("Guess the number in the length of", len1, "digits")

while test:
    player2_guess=input("Player2: Go ahead and guess the number: ")
    player2_guess.split()

    for number in player2_guess:
        numbers2.append(int(number))

    test=compare_fun(numbers1,numbers2, count, 2)
    count+=1

count2=count
count=0
test=True
numbers1.clear()
numbers2.clear()

player2_input=input("Player2: Enter the number you wish: ")
player2_input.split()

for number in player2_input:
    numbers2.append(int(number))
len2=len(numbers2)
print("Guess the number in the length of", len2, "digits")
while test:

    player1_guess=input("Player1: Go ahead and guess the number: ")
    player1_guess.split()

    for number in player1_guess:
        numbers1.append(int(number))

    test=compare_fun(numbers2,numbers1, count, 1)
    count+=1
count1=count

print()
print("Player 2 took", count2, "guesses to guess correctly")
print("Player 1 took", count1, "guesses to guess correctly")
print()

if count1<count2:
    print("Player 1 is Crowned the MasterMind.")
else:
    print("Player 2 is Crowned the MasterMind.")

print("Thank You For Playing The MasterMinds Game!!")



