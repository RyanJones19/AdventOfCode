import sys

data = [[c for c in s] for s in open(sys.argv[1]).read().strip().split("\n")]

R = len(data)
C = len(data[0])

letterMap = {
    "X": "M",
    "M": "A",
    "A": "S"
}

directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

def checkXMAS(row, col, letter, direction):
    if letter == "S":
        return 1
    count = 0
    nextLetter = letterMap[letter]
    if direction:
        rr = direction[0]
        cc = direction[1]
        if 0 <= row+rr < R and 0 <= col+cc < C:
            if data[row+rr][col+cc] == nextLetter:
                count += checkXMAS(row+rr, col+cc, nextLetter, (rr,cc))
    else:
        for rr, cc in directions:
            if 0 <= row+rr < R and 0 <= col+cc < C:
                if data[row+rr][col+cc] == nextLetter:
                    count += checkXMAS(row+rr, col+cc, nextLetter, (rr,cc))
    return count


total = 0
for r in range(R):
    for c in range(C):
        if data[r][c] == "X":
            total += checkXMAS(r, c, "X", None)

print(total)

total = 0

for r in range(R):
    for c in range(C):
        if data[r][c] == "A":
            if 0 <= r-1 and r+1 < R and 0 <= c-1 and c+1 < C:
                if (sorted([data[r-1][c-1], data[r+1][c+1]])== ["M","S"]) and (sorted([data[r+1][c-1], data[r-1][c+1]]) == ["M", "S"]):
                    total += 1

print(total)

