from collections import defaultdict

with open("day4Info.txt") as f:
    content = f.readlines()

def processCard(winningCard, myCard):
    totalMatches = 0
    for numSelection in myCard:
        if numSelection in winningCard and numSelection != "":
            totalMatches += 1
    return totalMatches


def part1(cardData):
    totalScore = 0

    for line in cardData:
        cardData = line.strip().split(":")[1]
        winningCard = cardData.split("|")[0].split(" ")
        myCard = cardData.split("|")[1].split(" ")

        totalMatches = processCard(winningCard, myCard)
        if totalMatches != 0:
            totalScore += 2**(totalMatches-1)
  
    return totalScore


def part2(data):
    deckOfCards = defaultdict(int)

    cardMapping = {}
    totalCards = 0
    for i, line in enumerate(data):
        deckOfCards[i+1] += 1
        cardId, card = line.split(':')
        winning, selections = card.split('|')
        winningNums = [int(x) for x in winning.split()]
        myNums = [int(x) for x in selections.split()]
        winningPicks = len(set(winningNums) & set(myNums))
        for j in range(winningPicks):
            deckOfCards[i+2+j] += deckOfCards[i+1]

        print(deckOfCards)
    return sum(deckOfCards.values())

print("Answer 1: " + str(part1(content)))
print("Answer 2: " + str(part2(content)))
