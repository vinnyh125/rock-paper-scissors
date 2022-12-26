import random

options = ['rock', 'paper', 'scissors']
gameStatus = ['1','2']

print('Welcome to rock paper scissors!')

gameCont = input("Press '1' to start; press '2' to quit: ")

while gameCont not in gameStatus:
    gameCont = input("That's not one of the options. Please try again: ")

if gameCont == '2':
    quit()

while gameCont == '1':

    compChoice = options[random.randint(0,2)]
    userChoice = input("Please type in 'rock', 'paper', or 'scissors': ")

    while userChoice not in options:
        print("That's an invalid input; please try again")
        userChoice = input("Please type in 'rock', 'paper', or 'scissors': ")

    while userChoice == compChoice:
        print('You chose: ' + userChoice)
        print('Computer chose: ' + compChoice)
        print('You tied.')

        compChoice = options[random.randint(0,2)]
        userChoice = input('Please type in your new choice: ')

        while userChoice not in options:
            print("That's an invalid input; please try again")
            userChoice = input("Please type in your new choice: ")

    if userChoice == 'rock' and compChoice == 'paper':
        print('You chose: ' + userChoice)
        print('Computer chose: ' + compChoice)
        print('You lose.')
    elif userChoice == 'rock' and compChoice == 'scissors':
        print('You chose: ' + userChoice)
        print('Computer chose: ' + compChoice)
        print('You won!')
    if userChoice == 'paper' and compChoice == 'rock':
        print('You chose: ' + userChoice)
        print('Computer chose: ' + compChoice)
        print('You won!')
    elif userChoice == 'paper' and compChoice == 'scissors':
        print('You chose: ' + userChoice)
        print('Computer chose: ' + compChoice)
        print('You lose.')
    if userChoice == 'scissors' and compChoice == 'rock':
        print('You chose: ' + userChoice)
        print('Computer chose: ' + compChoice)
        print('You lose.')
    elif userChoice == 'scissors' and compChoice == 'paper':
        print('You chose: ' + userChoice)
        print('Computer chose: ' + compChoice)
        print('You won!')  

    gameCont = input("Press '1' to continue; press '2' to quit: ")
