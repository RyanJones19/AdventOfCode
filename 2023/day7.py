import sys
from collections import defaultdict, Counter
import itertools as it


handTypes = ['five of a kind', 'four of a kind', 'full house', 'three of a kind', 'two pair', 'one pair', 'high card']
handTypes.reverse()
cardStrength = '23456789TJQKA'
cardStrengthPart2 = 'J23456789TQKA'

handTypeMap = defaultdict(list)
handTypeMapWithWilds = defaultdict(list)

data = open(sys.argv[1]).read().strip()

hands = data.split('\n')

def getMostFrequentHighestCard(hand: str) -> str:
    mostFrequentCard = sorted(Counter(hand).most_common(), key=lambda x:(x[1],cardStrengthPart2.index(x[0])), reverse=True)[0][0]
    if mostFrequentCard == 'J' and len(set(hand)) > 1:
        secondMostFrequentCard = sorted(Counter(hand).most_common(), key=lambda x:(x[1],cardStrengthPart2.index(x[0])), reverse=True)[1][0]
        return secondMostFrequentCard
    return mostFrequentCard


def processHandType(hand: str) -> None:
    hand, wager = hand.split()
    uniqueCards = set(hand)
    if len(uniqueCards) == 1:
        handTypeMap['five of a kind'].append((hand, wager))
    elif len(uniqueCards) == 2:
        handTypeMap['four of a kind'].append((hand, wager)) if any([hand.count(card) == 4 for card in uniqueCards]) else handTypeMap['full house'].append((hand, wager))
    elif len(uniqueCards) == 3:
        handTypeMap['three of a kind'].append((hand, wager)) if any([hand.count(card) == 3 for card in uniqueCards]) else handTypeMap['two pair'].append((hand, wager))
    elif len(uniqueCards) == 4:
        handTypeMap['one pair'].append((hand, wager))
    else:
        handTypeMap['high card'].append((hand, wager))

def processHandTypeWithWilds(hand: str) -> None:
    hand, wager = hand.split()
    bestHand = hand
    if "J" in hand:
        bestCardInHand = getMostFrequentHighestCard(hand)
        bestHand = hand.replace("J", bestCardInHand)
    uniqueCards = set(bestHand)
    if len(uniqueCards) == 1: 
        handTypeMapWithWilds['five of a kind'].append((hand, wager, bestHand))
    elif len(uniqueCards) == 2:
        handTypeMapWithWilds['four of a kind'].append((hand, wager, bestHand)) if any([bestHand.count(card) == 4 for card in uniqueCards]) else handTypeMapWithWilds['full house'].append((hand, wager, bestHand))
    elif len(uniqueCards) == 3:
        handTypeMapWithWilds['three of a kind'].append((hand, wager, bestHand)) if any([bestHand.count(card) == 3 for card in uniqueCards]) else handTypeMapWithWilds['two pair'].append((hand, wager, bestHand))
    elif len(uniqueCards) == 4:
        handTypeMapWithWilds['one pair'].append((hand, wager, bestHand))
    else:
        handTypeMapWithWilds['high card'].append((hand, wager, bestHand))

def sortDictByHandType(dict: dict) -> dict:
    dictKeys = list(dict.keys())
    dictKeys.sort(key=lambda x: handTypes.index(x))
    return {key: dict[key] for key in dictKeys}

def sortHandsByCardStrength(hands: list, cardStrength: str) -> list:
    return sorted(hands, key=lambda x: (cardStrength.index(x[0][0]), cardStrength.index(x[0][1]), cardStrength.index(x[0][2]), cardStrength.index(x[0][3]), cardStrength.index(x[0][4])))

def computeTotalWinnings(map: dict, cardStrength: str, processingFunc) -> int:
    for hand in hands:
        processingFunc(hand)

    handTypeMap = sortDictByHandType(map)
    sortedHands = [hands for handType in handTypeMap for hands in sortHandsByCardStrength(handTypeMap[handType], cardStrength)]

    totalWinnings = 0
    for rank, hand in enumerate(sortedHands):
        totalWinnings += (rank + 1) * int(hand[1])

    return totalWinnings

print(f'Part 1: {computeTotalWinnings(handTypeMap, cardStrength, processHandType)}')
print(f'Part 2: {computeTotalWinnings(handTypeMapWithWilds, cardStrengthPart2, processHandTypeWithWilds)}')

