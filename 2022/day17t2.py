import sys
import time
from copy import deepcopy

class h_bar:
    def __init__(self):
        self.tile_1 = (0, 2)
        self.tile_2 = (0, 3)
        self.tile_3 = (0, 4)
        self.tile_4 = (0, 5)
        self.height = 1
        self.points = []
        self.shape = "hbar"
        self.set_points()

    def set_points(self):
        self.points = [self.tile_1, self.tile_2, self.tile_3, self.tile_4]

class v_bar:
    def __init__(self):
        self.tile_1 = (0, 2)
        self.tile_2 = (1, 2)
        self.tile_3 = (2, 2)
        self.tile_4 = (3, 2)
        self.height = 4
        self.points = []
        self.shape = "vbar"
        self.set_points()

    def set_points(self):
        self.points = [self.tile_1, self.tile_2, self.tile_3, self.tile_4]

class square:
    def __init__(self):
        self.tile_1 = (0, 2)
        self.tile_2 = (0, 3)
        self.tile_3 = (1, 2)
        self.tile_4 = (1, 3)
        self.height = 2
        self.points = []
        self.shape = "square"
        self.set_points()

    def set_points(self):
        self.points = [self.tile_1, self.tile_2, self.tile_3, self.tile_4]

class l_shape:
    def __init__(self):
        self.tile_1 = (2, 2)
        self.tile_2 = (1, 4)
        self.tile_3 = (2, 4)
        self.tile_4 = (2, 3)
        self.tile_5 = (0, 4)
        self.height = 3
        self.points = []
        self.shape = "l"
        self.set_points()

    def set_points(self):
        self.points = [self.tile_1, self.tile_2, self.tile_3, self.tile_4, self.tile_5]

class plus_shape:
    def __init__(self):
        self.tile_1 = (1, 2)
        self.tile_2 = (0, 3)
        self.tile_3 = (1, 3)
        self.tile_4 = (2, 3)
        self.tile_5 = (1, 4)
        self.height = 3
        self.points = []
        self.shape = "plus"
        self.set_points()

    def set_points(self):
        self.points = [self.tile_1, self.tile_2, self.tile_3, self.tile_4, self.tile_5]

class game:
    def __init__(self):
        self.board = [['_' for _ in range(7)]]
        self.height = 1
        self.active_points = []
        self.active_shape = None

    def print(self):
        for row in self.board:
            printable_row = ""
            for col in row:
                printable_row += col
            print(printable_row)
        print()

    def add_shape(self, shape):
        self.active_points = shape.points
        self.active_shape = shape
        for _ in range(self.active_shape.height + 3):
            self.board.insert(0, ['.' for _ in range(7)])
        for point in shape.points:
            self.board[point[0]][point[1]] = '@'

    def shift(self, direction):
        if direction == '<':
            if self.active_points[0][1] != 0:
                next_points = list(map(lambda x: True if self.board[x[0]][x[1] - 1] in ['.', '@'] else False, self.active_points))
                if all(next_points):
                    while self.active_points:
                        cur_point = self.active_points.pop(0)
                        self.board[cur_point[0]][cur_point[1]] = '.'

                    self.active_shape.tile_1 = (self.active_shape.tile_1[0], self.active_shape.tile_1[1] - 1)
                    self.active_shape.tile_2 = (self.active_shape.tile_2[0], self.active_shape.tile_2[1] - 1)
                    self.active_shape.tile_3 = (self.active_shape.tile_3[0], self.active_shape.tile_3[1] - 1)
                    self.active_shape.tile_4 = (self.active_shape.tile_4[0], self.active_shape.tile_4[1] - 1)
                    if self.active_shape.shape in ["l", "plus"]:
                        self.active_shape.tile_5 = (self.active_shape.tile_5[0], self.active_shape.tile_5[1] - 1)
                    self.active_shape.set_points()

                    self.active_points = self.active_shape.points

                    for point in self.active_points:
                        self.board[point[0]][point[1]] = '@'

        elif direction == '>':
            if self.active_points[-1][1] != 6:
                next_points = list(map(lambda x: True if self.board[x[0]][x[1] + 1] in ['.', '@'] else False, self.active_points))
                if all(next_points):
                    while self.active_points:
                        cur_point = self.active_points.pop(0)
                        self.board[cur_point[0]][cur_point[1]] = '.'

                    self.active_shape.tile_1 = (self.active_shape.tile_1[0], self.active_shape.tile_1[1] + 1)
                    self.active_shape.tile_2 = (self.active_shape.tile_2[0], self.active_shape.tile_2[1] + 1)
                    self.active_shape.tile_3 = (self.active_shape.tile_3[0], self.active_shape.tile_3[1] + 1)
                    self.active_shape.tile_4 = (self.active_shape.tile_4[0], self.active_shape.tile_4[1] + 1)
                    if self.active_shape.shape in ["l", "plus"]:
                        self.active_shape.tile_5 = (self.active_shape.tile_5[0], self.active_shape.tile_5[1] + 1)
                    self.active_shape.set_points()

                    self.active_points = self.active_shape.points

                    for point in self.active_points:
                        self.board[point[0]][point[1]] = '@'


    def fall(self) -> bool:
        next_points = list(map(lambda x: (x[0] + 1, x[1]), self.active_points))
        can_fall = True
        for point in next_points:
            if self.board[point[0]][point[1]] in ['_', '#']:
                can_fall = False
                break
        if can_fall:
            while self.active_points:
                cur_point = self.active_points.pop(0)
                self.board[cur_point[0]][cur_point[1]] = '.'
            self.active_points = next_points
            if self.active_shape.shape in ["hbar", "vbar", "square"]:
                self.active_shape.tile_1, self.active_shape.tile_2, self.active_shape.tile_3, self.active_shape.tile_4 = self.active_points
            else:
                self.active_shape.tile_1, self.active_shape.tile_2, self.active_shape.tile_3, self.active_shape.tile_4, self.active_shape.tile_5 = self.active_points
            self.active_shape.points = next_points
            for point in self.active_points:
                self.board[point[0]][point[1]] = '@'
        else:
            for point in self.active_points:
                self.board[point[0]][point[1]] = '#'
            self.board = [row for row in self.board if set(row) != {'.'}]

        return can_fall


game = game()
shape_order = [h_bar(), plus_shape(), l_shape(), v_bar(), square()]
shape_order_index = -1
air_flow_index = -1
dropped_shapes = 0
air_flow_pattern = open(sys.argv[1]).read().strip()

while dropped_shapes < 2022:
    shape_order_index = (shape_order_index + 1) % len(shape_order)
    next_shape = shape_order[shape_order_index]
    next_shape.__init__()
    game.add_shape(next_shape)
    game.print()
    air_flow_index = (air_flow_index + 1) % len(air_flow_pattern)
    next_movement = air_flow_pattern[air_flow_index]
    game.shift(next_movement)
    game.print()
    while(game.fall()):
        time.sleep(0.5)
        game.print()
        air_flow_index = (air_flow_index + 1) % len(air_flow_pattern)
        next_movement = air_flow_pattern[air_flow_index]
        game.shift(next_movement)
        game.print()
    dropped_shapes += 1

print(f"Height of Tower is {len(game.board) - 1}")



