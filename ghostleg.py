#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys

LOTTERY_SELECTORS = ["a", "b", "c", "d", "e"]
LOTTERY_PRIZE = [i.upper() for i in LOTTERY_SELECTORS]
LOTTERY_HEIGHT = 5

def generate_ladders():
    # target array 5 * 10
    idx = 0
    ladders = []
    for _ in range(LOTTERY_HEIGHT):
        layer = []
        prev_is_ladder = False
        for _ in range(len(LOTTERY_SELECTORS) - 1):
            if prev_is_ladder:
                prev_is_ladder = False
                layer.append(0)
                continue

            num = random.randint(1, 999999)
            if num % 2 == 0:
                layer.append(1)
                prev_is_ladder = True
            else:
                layer.append(0)

            idx += 1
        ladders.append(layer)
        prev_is_ladder = False

    return ladders



def display_ladders(ladders):
    print (' ' * 5).join(LOTTERY_SELECTORS)

    for i in range(LOTTERY_HEIGHT):
        for j, _ in enumerate(LOTTERY_SELECTORS):
            sys.stdout.write('|')
            sys.stdout.write(' ' * 5)
        sys.stdout.write('\n')

        for j, _ in enumerate(LOTTERY_SELECTORS):
            sys.stdout.write('|')
            if j > len(LOTTERY_SELECTORS) - 2:
                break
            if ladders[i][j]:
                sys.stdout.write('-' * 5)
            else:
                sys.stdout.write(' ' * 5)

        sys.stdout.write('\n')

    print (' ' * 5).join(LOTTERY_PRIZE)

"""
  (x, h) left ladder: (x-1, h)
  (x, h) right ladder: (x, h)

  a    b    c    d    e

  │    │    │    │    │
  │    ├────┤    ├────┤
  │         │    │    │
  ├── 1,1   │    │    │
  │         │    │    │
  ├────┤    ├────┤    │
  │    │         │    │
  │    ├── x,h   │    │
  │    │         │    │
  ├────┤    │    ├────┤
  │    │    │    │    │
  │    │    │    │    │
  │    │    │    │    │
  │    │    │    │    │
  │    │    │    │    │
  │    │    │    │    │
"""
def get_exit(sel, ladders):
    x = LOTTERY_SELECTORS.index(sel)
    h = 0

    while h < LOTTERY_HEIGHT:
        left, right = False, False
        if x < 1:
            left = False
            right = ladders[h][x] > 0
        elif x > len(LOTTERY_SELECTORS) - 2:
            left = ladders[h][x-1] > 0
            right = False
        else:
            left = ladders[h][x-1] > 0
            right = ladders[h][x] > 0

        if left:
            x -= 1
        elif right:
            x += 1

        h += 1

    return LOTTERY_PRIZE[x]

def demo():
    ladders = generate_ladders()
    print "raw ladders", ladders
    print

    display_ladders(ladders)

    print
    for sel in LOTTERY_SELECTORS:
        print '%s -> %s' % (sel, get_exit(sel, ladders))


if __name__ == "__main__":
    demo()
