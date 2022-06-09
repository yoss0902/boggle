from boggle_board_randomizer import *
from time import *


class BoggleGame:

    def __init__(self, words, board):
        self.board = board
        self.time = 3
        self.words = words
        self.score = 0
        self.word_lst = []
        self.path = []
        self.word = ""

    def available_cell_to_choose(self, row, col):
        sorraunding_coordinates = [(row + 1, col), (row - 1, col), (row - 1, col - 1), (row, col - 1),
                                   (row + 1, col - 1), (row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]
        coordinates_to_delete = []
        if row + 1 > len(self.board):
            coordinates_to_delete.extend([(row + 1, col), (row + 1, col - 1), (row + 1, col + 1)])
        if row - 1 < 0:
            coordinates_to_delete.extend([(row - 1, col), (row - 1, col - 1), (row - 1, col + 1)])
        if col - 1 < 0:
            coordinates_to_delete.extend([(row - 1, col - 1), (row, col - 1), (row + 1, col - 1)])
        if col + 1 > len(self.board[0]):
            coordinates_to_delete.extend([(row - 1, col + 1), (row, col + 1), (row + 1, col + 1)])
        deleting_coordinates = list(set(coordinates_to_delete))
        for i in deleting_coordinates:
            if i in sorraunding_coordinates:
                sorraunding_coordinates.remove(i)
        return sorraunding_coordinates

    def updating_variables(self, row, col):
        self.word += self.board[row][col]
        self.path.append((row, col))
        if self.word in self.words and self.word not in self.word_lst:
            self.word_lst.append(self.word)
            self.score += len(self.path) ** 2
            self.word = ""
            self.path = []







g = BoggleGame(['ITS', 'GZC', 'TSC', 'ESQU', 'ZTC'])
start = time()
print(g.available_cell_to_choose(0, 0))
end = time()
