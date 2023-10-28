import random
import numpy as np
from tqdm import trange
from typing import List


prob1 = .55
prob2 = .35
prob3 = .10

marbles1 = 48
marbles2 = 48
marbles3 = 48

class Marble(object):
    def __init__(self, id, color):
        self.id = id
        self.color = color
        self.drawn = False

    def __repr__(self):
        return f"Marble {self.id} ({self.color})"


def draw_marble_with_replace(bags: List[List[Marble]]):
    r = random.random()
    bag: List[Marble] = None
    if r < prob1:
        bag = bags[0]
    elif r < prob1 + prob2:
        bag = bags[1]
    else:
        bag = bags[2]
    marble = random.choice(bag)
    marble.drawn = True
    return marble


def draw_marble_without_replace(bags: List[List[Marble]]):
    # shit perf but don't care
    marble = draw_marble_with_replace(bags)
    while marble.drawn:
        marble = draw_marble_with_replace(bags)
    return marble


if __name__ == "__main__":
    bag1 = []
    bag2 = []
    bag3 = []

    for i in range(marbles1):
        bag1.append(Marble(i, "black"))
    for i in range(marbles1, marbles1 + marbles2):
        bag2.append(Marble(i, "silver"))
    for i in range(marbles1 + marbles2, marbles1 + marbles2 + marbles3):
        bag3.append(Marble(i, "gold"))

    bags = [bag1, bag2, bag3]

    # monte carlos
    sims = []
    for i in trange(2000):
        draw_count = 0
        drawn_marbles = set()
        while len(drawn_marbles) < 144:
            marble = draw_marble_with_replace(bags)
            draw_count += 1
            if marble.id not in drawn_marbles:
                drawn_marbles.add(marble.id)
                # print(f"Drew new {marble}")

        sims.append(draw_count)
        # print(f"Number of draws: {draw_count}")
    
    print(np.mean(sims))
