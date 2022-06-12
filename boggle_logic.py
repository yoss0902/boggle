from boggle_board_randomizer import *




class BoggleLogic:
    def __init__(self, board, words):
        self.word = ""
        self.word_path = []
        self.board = board
        self.words = words
        self.word_lst = []
        self.score = 0


    def available_cell_to_choose(self, row, col):
        sorraunding_coordinates = [(row + 1, col), (row - 1, col), (row - 1, col - 1), (row, col - 1),
                                   (row + 1, col - 1), (row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]
        coordinates_to_delete = []
        if row + 1 >= len(self.board):
            coordinates_to_delete.extend([(row + 1, col), (row + 1, col - 1), (row + 1, col + 1)])
        if row - 1 < 0:
            coordinates_to_delete.extend([(row - 1, col), (row - 1, col - 1), (row - 1, col + 1)])
        if col - 1 < 0:
            coordinates_to_delete.extend([(row - 1, col - 1), (row, col - 1), (row + 1, col - 1)])
        if col + 1 >= len(self.board[0]):
            coordinates_to_delete.extend([(row - 1, col + 1), (row, col + 1), (row + 1, col + 1)])
        deleting_coordinates = list(set(coordinates_to_delete))
        for i in deleting_coordinates:
            if i in sorraunding_coordinates:
                sorraunding_coordinates.remove(i)
        return sorraunding_coordinates

    def updating_variables(self, row, col, time_flag):
        if time_flag:
            print(row, col)

            self.word += self.board[row][col]
            self.word_path.append((row, col))


    def check_complete_word(self, time_flag):
        if time_flag:
            self.word = ""
            self.word_path = []


    def all_cells(self):
        every_cell = []
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                every_cell.append((i,j))
        return every_cell

    def restart_game(self):
        self.word_lst = []
        self.word_path = []
        self.score = 0
        self.word = ""

    def set_board(self, board):
        self.board = board
