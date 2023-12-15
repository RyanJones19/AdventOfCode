import sys

data = open(sys.argv[1]).read().strip().split('\n')

sequences = {}

def processScore(board: str, splits: list[int], boardPosition: int, splitsPosition: int, objectInSplit: int) -> int:
    key = (boardPosition, splitsPosition, objectInSplit)
    if key in sequences:
        return sequences[key]
    if boardPosition == len(board):
        if splitsPosition == len(splits) and objectInSplit == 0:
            return 1
        elif splitsPosition == len(splits) - 1 and splits[splitsPosition] == objectInSplit:
            return 1
        else:
            return 0
    else:
        answer = 0
        for character in ['.', '#']:
            if board[boardPosition] == character or board[boardPosition] == '?':
                if character == '.' and splitsPosition < len(splits) and splits[splitsPosition] == objectInSplit:
                    answer += processScore(board, splits, boardPosition+1, splitsPosition+1, 0)
                elif character == '#':
                    answer += processScore(board, splits, boardPosition+1, splitsPosition, objectInSplit+1)
                elif character == '.' and objectInSplit == 0:
                    answer += processScore(board, splits, boardPosition+1, splitsPosition, objectInSplit)
        sequences[key] = answer
    return answer

for part2 in [False, True]:
    answers = []
    for line in data:
        sequences.clear()
        board, splits = line.split(' ')
        splits = [int(x) for x in splits.split(',')]
        if part2:
            board = ''.join([board + '?' if i < 4 else board for i in range(5)])
            splits = splits*5

        answers.append(processScore(board, splits, 0, 0, 0))
    print(f"Part {2 if part2 else 1}: {sum(answers)}")

