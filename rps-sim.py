#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time
import numpy as np
import matplotlib.pyplot as plt
import tqdm
import sys

# Created by Jakub Michniewicz (https://atomiccode,pl)

def game(showPrints=False):
    playerScore = 0
    aiScore = 0

    while (playerScore < 3 and aiScore < 3):

#         playerChoice = input('Input "r", "p", or "s": ')
        playerChoice = random.choice(('r', 'p', 's'))
        aiChoice = random.choice(('rock', 'paper', 'scissors'))

        if aiChoice == 'rock':
            if playerChoice == 'p':
                playerScore += 1
                if showPrints: print('You win the round')
            elif playerChoice == 's':
                aiScore += 1
                if showPrints: print('You lose the round')
            else:
                if showPrints: print('Draw')
                pass

        if aiChoice == 'paper':
            if playerChoice == 's':
                playerScore += 1
                if showPrints: print('You win the round')
            elif playerChoice == 'r':
                aiScore += 1
                if showPrints: print('You lose the round')
            else:
                if showPrints: print('Draw')
                pass

        if aiChoice == 'scissors':
            if playerChoice == 'r':
                playerScore += 1
                if showPrints: print('You win the round')
            elif playerChoice == 'p':
                aiScore += 1
                if showPrints: print('You lose the round')
            else:
                if showPrints: print('Draw')
                pass

        if showPrints: print(f'{playerScore}:{aiScore}')

    if playerScore == 3:
        if showPrints: print('You win the game')
        return 1
    else:
        if showPrints: print('You lose the game')
        return -1

def simulate(numberOfGames):
    playerWins = 0
    aiWins = 0

    for x in range(numberOfGames):
        result = game()

        if result == 1:
            playerWins += 1
        else:
            aiWins += 1

#     print(f'Total games: {numberOfGames}')
#     print(f'Player wins {playerWins} times')
#     print(f'AI wins {aiWins} times')

    return (playerWins, aiWins)


a = []
b = []

try:
    simulations = int(sys.argv[1])
except Exception as ex:
    print("Please input integer value for number of simulations")
    sys.exit()

startTime = time.time()

for i in tqdm.tqdm(range(simulations), ncols=100, desc="Simulating... "):
    a1, a2 = simulate(simulations)
    a.append(a1)
    b.append(a2)

x = range(1, len(a)+1)
averageA = sum(a)/len(a)
averageB = sum(b)/len(b)

print("--- Calculated in %s seconds ---" % (time.time() - startTime))

plt.stackplot(x, a, b, labels=['Player wins (avg. '+str(averageA)+')','AI wins (avg. '+str(averageB)+')'])
plt.legend(loc='upper left')

plt.show()
