from boggle_board_randomizer import *


class BoggleLogic:
    """a class for the logic of the Boggle game

    attributes:
            current guess word, word path, board, words dict,
            guessed words list and score

    methods:
            getters and setters
            available cells which return the cells around the last choice,
            updating variables which update the vars
            check complete word which update the vars
            all cells which return all cells in the board
            restart game which update the vars
    """

    def __init__(self, board, words):
        """a constructor which creates the vars of the game"""
        self.__word = ""
        self.__word_path = []
        self.__board = board
        self.__words = words
        self.__word_lst = []
        self.__score = 0

    @property
    def word(self):
        """word getter"""
        return self.__word

    @word.setter
    def word(self, new_word):
        """word setter"""
        self.__word = new_word

    @property
    def word_path(self):
        """word path getter"""
        return self.__word_path

    @word_path.setter
    def word_path(self, new_path):
        """word path setter"""
        self.__word_path = new_path

    @property
    def board(self):
        """board getter"""
        return self.__board

    @board.setter
    def board(self, new_board):
        """board setter"""
        self.__board = new_board

    @property
    def words(self):
        """words dict getter"""
        return self.__words

    @property
    def word_lst(self):
        """guessed words list getter"""
        return self.__word_lst

    @word_lst.setter
    def word_lst(self, new_word_lst):
        """guessed words list setter"""
        self.__word_lst = new_word_lst

    @property
    def score(self):
        """score getter"""
        return self.__score

    @score.setter
    def score(self, new_score):
        """score setter"""
        self.__score = new_score

    def available_cell_to_choose(self, row, col):
        """return the cells around the given index which are inside the board"""
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
        """update the variables after board button has been pressed"""
        if time_flag:
            self.word += self.board[row][col]
            self.word_path.append((row, col))

    def check_complete_word(self, time_flag, submit):
        """update the variables after submit button has been pressed"""
        if time_flag and len(self.word) >= 3:
            flag = False
            if self.word in self.words and self.word not in self.word_lst:
                self.word_lst.append(self.word)
                self.score += len(self.word_path) ** 2
                flag = True
            self.word_path = []
            submit(flag)
            self.word = ""

    def all_cells(self):
        """return every possible cells inside the board"""
        every_cell = []
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                every_cell.append((i, j))
        return every_cell

    def restart_game(self, board):
        """initialize the vars after the game start over"""
        self.word_lst = []
        self.word_path = []
        self.score = 0
        self.word = ""
        self.board = board
