# Coin flip Simulation

# Write some code that simulates flipping a single coin however many times the user decides. 
# The code should record the outcomes and count the number of tails and head

import random

def toss(flips):
    flip  = [random.randint(0,1) for i in range(flips)]
    coin  = ['Heads' if i == 1 else 'Tails' for i in flip]

    heads = sum([i =='Heads' for i in coin])
    tails = flips - heads

    print(f"Number of tails: {tails} out of {flips} coin flips")
    print(f"Number of heads: {heads} out of {flips} coin flips")

coin_flips = int(input("How many times would you like to toss a coin? "))
toss(coin_flips)
