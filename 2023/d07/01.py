import sys
import heapq
from collections import Counter

sys.path.append('..')
from utils import *


# Define a mapping of characters to their priority values
card_priority = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}


def hand_value(hand: str):
    # Countable counts the occurrences of each element in an iterable
    counts = Counter(hand)
    sorted_counts = sorted(counts.values(), reverse=True)

    # Determine the rank of the hand
    if sorted_counts == [5]:
        rank = 7  # Five of a Kind
    elif sorted_counts == [4, 1]:
        rank = 6  # Four of a Kind
    elif sorted_counts == [3, 2]:
        rank = 5  # Full House
    elif sorted_counts == [3, 1, 1]:
        rank = 4  # Three of a Kind
    elif sorted_counts == [2, 2, 1]:
        rank = 3  # Two Pair
    elif sorted_counts == [2, 1, 1, 1]:
        rank = 2  # One Pair
    else:
        rank = 1  # High Card

    # Combine rank with individual card values for tie-breaking
    value = (rank, [card_priority[c] for c in hand])
    return value


def challenge_1(filename: str):
    lines = readfile(filename)

    hand_bids = []
    for line in lines:
        line = split_line(line, " ")
        hand_bids.append((line[0], line[1]))

    # print(hand_bids)

    # Max-heap
    priority_queue = []
    for hand_bid in hand_bids:
        heapq.heappush(priority_queue, (hand_value(hand_bid[0]), (hand_bid[0], int(hand_bid[1]))))

    output = 0
    i = 1
    while priority_queue:
        tmp = heapq.heappop(priority_queue)[1]
        # print("Rank ", i, "\thand ", tmp[0], "\tbid ", tmp[1])
        output += i * tmp[1]
        i += 1
    print("Solution: ", output)


# f = "data/simple.txt"
f = "data/challenge.txt"
challenge_1(f)
