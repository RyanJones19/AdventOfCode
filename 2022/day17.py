import sys
import time
from itertools import cycle
from copy import deepcopy

movements = open(sys.argv[1]).read().strip()

class horizontal_bar():
    def __init__(self):
        self.shape = [[('.', 'e'), ('.', 'e'), ('@', 'hb'), ('@', 'hb'), ('@', 'hb'), ('@', 'hb'), ('.', 'e')]]
    def shift(self, row, direction):
        if direction == '<':
            if row[0] == ('.', 'e'):
                del row[0]
                row.append(('.','e'))
                return row
        if direction == '>':
            if row[6] == ('.', 'e'):
                del row[6]
                row.insert(0, ('.', 'e'))
                return row


class vertical_bar():
    def __init__(self):
        self.shape = [[('.','e'), ('.', 'e'), ('@', 'vb'), ('.', 'e'), ('.', 'e'), ('.', 'e'), ('.', 'e')],
                      [('.','e'), ('.', 'e'), ('@', 'vb'), ('.', 'e'), ('.', 'e'), ('.', 'e'), ('.', 'e')],
                      [('.','e'), ('.', 'e'), ('@', 'vb'), ('.', 'e'), ('.', 'e'), ('.', 'e'), ('.', 'e')],
                      [('.','e'), ('.', 'e'), ('@', 'vb'), ('.', 'e'), ('.', 'e'), ('.', 'e'), ('.', 'e')]
                      ]
    def shift(self, row, direction):
        if direction == '<':

            if row[0] == ('.', 'e'):
                #map(lambda x: (x[1], x[0]) if x[0] == '@' and my_list[my_list.index(x) - 1][0] == '.' else x, row)
                #map(lambda x: , row)
                del row[0]
                row.append(('.','e'))
                return row
        if direction == '>':
            if row[6] == ('.', 'e'):
                del row[6]
                row.insert(0, ('.', 'e'))
                return row


class plus_sign():
    pass

class L_shape():
    pass

class square():
    pass

class game():
    def __init__(self):
        self.board = [[('_', 'f') for _ in range(7)]]
        self.hb = horizontal_bar()
        self.vb = vertical_bar()

    def print(self):
        print()
        print("==============")
        for row in self.board:
            board_row = ''
            for column in row:
                board_row += column[0]
            print(board_row)
        print("==============")

    def drop_new_shape(self, shape):
        self.board[:0] = [[('.', 'e') for _ in range(7)] for _ in range(3)]
        for row in shape.shape:
            self.board.insert(0, row)

    def shift(self, direction):
        print(f"MOVING {direction}")
        for row in self.board[::-1]:
            if set(row) == set([('_', 'f')]):
                continue
            else:
                for brick, btype in row:
                    if btype == 'hb' and brick != '#':
                        row = self.hb.shift(row, direction)
                        break
                    if btype == 'vb' and brick != '#':
                        row = self.vb.shift(row, direction)
                        break

    def fall(self) -> bool:
        print("Trying to fall")
        inverted_board = self.board[::-1]
        for row_num, row in enumerate(inverted_board):
            can_merge = True
            if row_num < len(inverted_board) - 1:
                zipped_rows = list(zip(row, inverted_board[row_num+1]))
                new_row = list()
                for merged_point in zipped_rows:
                    if len(set(zipped_rows)) == 1:
                        new_row = row
                        break
                    if (('.', 'e')) not in merged_point:
                        can_merge = False
                        new_row = row
                        break
                    else:
                        if set(merged_point) == set([('.', 'e')]):
                            new_row.append(('.', 'e'))
                            continue
                        for point in merged_point:
                            if point == (('.', 'e')):
                                continue
                            else:
                                new_row.append(point)
                                break
                if can_merge:
                    inverted_board[row_num] = new_row
                    if row_num + 1 != len(inverted_board) - 1 and row_num != 0:
                        inverted_board[row_num + 1] = [('.', 'e') for _ in range(7)]
            elif row_num == len(inverted_board) - 1:
                zipped_rows = list(zip(row, inverted_board[row_num-1]))
                new_row = list()
                for merged_point in zipped_rows:
                    if (('.', 'e')) not in merged_point or len(set(zipped_rows)) == 1:
                        can_merge = False
                        new_row = row
                        break
                    else:
                        for point_num, point in enumerate(merged_point):
                            if point == (('.', 'e')) and point_num == 0:
                                continue
                            else:
                                new_row.append(point)
                                break
                inverted_board[row_num-1] = new_row
                inverted_board[row_num] = [('.', 'e') for _ in range(7)]

        if self.board == inverted_board[::-1]:
            print("no rocks could fall, will drop new rock")
            for r, row in enumerate(self.board):
                for c, col in enumerate(row):
                    if col[0] == '@':
                        self.board[r][c] = ('#', self.board[r][c][1])
            return False
        self.board = inverted_board[::-1]
        return True

                        




game = game()
dropped_bricks = 0
bricks = [horizontal_bar(), vertical_bar()]
inf_cycle = cycle(bricks)
air_stream = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
air_stream_index = 0

while(dropped_bricks) < 5:
    next_brick = next(inf_cycle)
    next_brick.__init__()
    game.drop_new_shape(next_brick)
    next_air_stream_direction = air_stream[air_stream_index]
    air_stream_index = (air_stream_index + 1) % len(air_stream)
    game.print()
    game.shift(next_air_stream_direction)
    game.print()
    while(game.fall()):
        game.print()
        next_air_stream_direction = air_stream[air_stream_index]
        air_stream_index = (air_stream_index + 1) % len(air_stream)
        game.shift(next_air_stream_direction)
        game.print()
        time.sleep(1)

    while(set(game.board[0]) == set([('.', 'e')])):
        game.board.pop(0)
    dropped_bricks += 1
    print("Rocks came to rest in final position")
    game.print()


