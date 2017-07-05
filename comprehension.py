import random  # importing module named:random

guessesTaken = 0  # assign 0 to variable guessesTaken

print('Hello! What is your name?')  # prints 'Hello! What is your name?' in terminal
myName = input()  # asks the user input (his/her name) and assign it to variable myName

number = random.randint(1, 20)  # assign a random integer between 1 and 20 to variable 'number '
#  prints Well, given name, I am thinking of a number between 1 and 20 in terminal.
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:  # while the value of variable guessesTaken is lower then 6 :
    print('Take a guess.')  # prints to terminal
    guess = input()  # asks for an input which will be assigned to variable guess
    guess = int(guess)  # converts variable guess(string)to integer and assigns it to variable guess

    guessesTaken += 1  # increase guessesTaken variable's value by 1

    if guess < number:  # if guess variable is lower then number variable (the random generated number between 1 and 20)
        print('Your guess is too low.')  # prints to terminal

    if guess > number:  # if guess variable is higher then number variable
        print('Your guess is too high.')  # prints to terminal

    if guess == number:  # if guess variable is equal to number variable
        break  # break out of the loop

if guess == number:  # if guess variable is equal to number variable :
    guessesTaken = str(guessesTaken)  # converts guessesTaken(int) variable to string
    # prints to terminal ,where myname variable's value is the given name and guessesTaken is the number of the guesses
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:  # if guess variable is not equal to number variable :
    number = str(number)  # converts number(int) variable to string
    # prints to terminal where number variable's value is the random guess number
    print('Nope. The number I was thinking of was ' + number)
