'''
Made by Michał "umikali" Wójtowicz
on April 1st 2023
'''

print("\033[2J\033[1;1H")

from random import randint


print("Don't know how to play? Visit https://www.world-of-board-games.com.sg/docs/Super-Farmer.pdf")

numberOfPlayers = int(input('Enter how many players are going to play.\n>'))

players = [] # all of the players in one list

for i in range(numberOfPlayers):
    players.append([1, 0, 0, 0, 0, 0, 0])

animal = ('rabbit', 'sheep', 'pig', 'cow', 'horse')

def trade(WhichPlayer):
    print('''Exchange chart
1 sheep = 6 rabbits,
1 pig = 2 sheep,
1 cow = 3 pigs,
1 horse = 2 cows,
1 small dog = 1 sheep,
1 big dog = 1 cow.''')
    print('What do you want to buy?')
    print('1) sheep')
    print('2) pig')
    print('3) cow')
    print('4) horse')
    print('5) small dog')
    print('6) big dog')
    whichAnimal = int(input('enter a number from 1 to 6 : '))
    animals = ('rabbits', 'sheep', 'pigs', 'cows', 'horses', 'small dogs', 'big dogs')
    animalName = animals[whichAnimal]
    howManyAnimals = int(input('how many ' + animalName + ' do you want to buy?\n>'))
    if   whichAnimal == 1: times = 6; animalToExchange = 0
    elif whichAnimal == 2: times = 2; animalToExchange = 1
    elif whichAnimal == 3: times = 3; animalToExchange = 2
    elif whichAnimal == 4: times = 2; animalToExchange = 3
    elif whichAnimal == 5: times = 1; animalToExchange = 1
    elif whichAnimal == 6: times = 1; animalToExchange = 3
    if players[WhichPlayer][animalToExchange] > howManyAnimals * times:
        print("That'll be ", howManyAnimals * times, ' ', animals[animalToExchange])
        players[WhichPlayer][animalToExchange] -= howManyAnimals * times # substract the amount from the players' balance
        players[WhichPlayer][whichAnimal] += howManyAnimals
    else:
        q = input("you can't buy that many. do you want to try again? (Y/n) >").lower()
        if q == 'y' or q == '':
            trade(WhichPlayer) # I know this allows for the player to do a stack overflow, but who cares?
            return

def printData(listOfAnimals):
    print('you have ', str(listOfAnimals[0]), ' rabbits')
    print('you have ', str(listOfAnimals[1]), ' sheep')
    print('you have ', str(listOfAnimals[2]), ' pigs')
    print('you have ', str(listOfAnimals[3]), ' cows')
    print('you have ', str(listOfAnimals[4]), ' horses')
    print('you have ', str(listOfAnimals[5]), ' small dog')
    print('you have ', str(listOfAnimals[6]), ' big dog')

def roll(WhichPlayer):
    animals = ('rabbit', 'sheep', 'pig', 'cow', 'horse', 'fox', 'wolf')
    dice1 = (0,0,0,0,0,0,1,1,2,2,4,5)
    dice2 = (0,0,0,0,0,0,1,1,1,2,3,6)
    rolled = randint(0, 11)
    rolled2 = randint(0, 11)
    print ('the first dice rolled ', animals[dice1[rolled]])
    print('the second dice rolled ', animals[dice2[rolled2]])
    animalint = dice1[rolled]
    if animalint == 5:
        if players[WhichPlayer][5] > 0:
            players[WhichPlayer][5] -= 1
            print('You lost a small dog.')
            return
        else:
            players[WhichPlayer][0] = 1
            print('You lost all your rabbits!')
    else:
        if animalint == dice2[rolled2]:
            players[WhichPlayer][animalint] += int((players[WhichPlayer][animalint] + 2) / 2)
        else:
            players[WhichPlayer][animalint] += int((players[WhichPlayer][animalint] + 1) / 2)
    animalint = dice2[rolled2]
    if animalint == 6:
        if players[WhichPlayer][6] > 0:
            players[WhichPlayer][6] -= 1
            print('You lost a big Dog!')
            return
        else:
            players[WhichPlayer][0] = 1
            players[WhichPlayer][1] = 0
            players[WhichPlayer][2] = 0
            players[WhichPlayer][3] = 0
            print('You lost all of your animals except your horses!')
    else:
        players[WhichPlayer][animalint] += int((players[WhichPlayer][animalint] + 1) / 2)

global run
run = True

def checkForWin(WhichPlayer):
    global run
    for i in range(0, 5):
        if players[WhichPlayer][i] < 1:
            return
    run = False
    print('Congratulations, Player ' + str(WhichPlayer + 1) + ' you won!')



print("\033[2J\033[1;1H") # clear the screen
while run: # stop the game when run is set to False
    for i in range(len(players)): # loop trough all the players
        print('Player ', i + 1, )
        printData(players[i])
        tradeQuestion = input('Do you want to trade? (y/N) >').lower()
        if tradeQuestion == "y":
            trade(i)
        elif tradeQuestion == "n" or tradeQuestion == "":
            print('ok.')
        else:
            print("I'll take that as a no.")
        print("\033[2J\033[1;1H") # clear the screen
        roll(i)
        checkForWin(i)


