from boggle_board_randomizer import *
from copy import deepcopy
import tkinter as tk
from tkinter import messagebox
from boggle_logic import *
from boggle_widgets import *
import sys

class Boggle:
    """a class for the graphical user interface in addition to the main

      attributes:
            words dict, root, frame, timer, button board, game logic,
            score, guess, guessed word list, start button, rules, submit button

      methods:
            getters, setters
            updating variables when board button has been pressed,
            restart game and variables
            exit game
      """

    def __init__(self, words, board):
        """ the game constructor which creates the widgets
        and the mainloop of the game"""
        self.__words = words
        self.__root = tk.Tk()
        self.root.title(GAME_TITLE)
        self.__outer_frame = OuterFrame(self.root)
        self.__time = Timer(self.outer_frame.frame, self.restart_game, self.exit)
        self.__board = Board(self.outer_frame.frame, self.updating_variables, board)
        self.__boggle_logic = BoggleLogic(self.board.board, self.words)
        self.__score = Score(self.outer_frame.frame)
        self.__current_guess = CurrentGuess(self.outer_frame.frame)
        self.__word_lst = WordLst(self.outer_frame.frame)
        self.__start_button = StartButton(self.outer_frame.frame, self.time, self.board)
        self.__rules = Rules(self.outer_frame.frame)
        self.__submit = Submit(self.outer_frame.frame, self.time, self.logic, self.word_lst,
                               self.guess, self.score, self.board, self.words)
        self.__image = Image(self.outer_frame.frame)

    @property
    def words(self):
        """words dict getter"""
        return self.__words

    @property
    def root(self):
        """root dict getter"""
        return self.__root

    @property
    def outer_frame(self):
        """outer frame dict getter"""
        return self.__outer_frame

    @property
    def time(self):
        """timer getter"""
        return self.__time

    @property
    def board(self):
        """board getter"""
        return self.__board

    @property
    def logic(self):
        """boggle logic getter"""
        return self.__boggle_logic

    @property
    def score(self):
        """score getter"""
        return self.__score

    @property
    def guess(self):
        """guess getter"""
        return self.__current_guess

    @property
    def word_lst(self):
        """words guessed getter"""
        return self.__word_lst

    @property
    def start_button(self):
        """start button getter"""
        return self.__start_button

    @property
    def rules(self):
        """rules button getter"""
        return self.__rules

    @property
    def submit(self):
        """submit button getter"""
        return self.__submit

    @property
    def image(self):
        """image getter"""
        return self.image

    def run(self):
        """run the mainloop of the GUI"""
        self.root.mainloop()

    def updating_variables(self, row, col):
        """ updating the variable each time a board
        button have been pressed"""
        if self.time.time_flag:
            def letter_press():
                self.logic.updating_variables(row, col, self.time.time_flag)
                available_cells = self.logic.available_cell_to_choose(row, col)
                self.board.lock_and_unlock_buttons(available_cells, self.logic.word_path)
                self.guess.update_guess(f" {INITIAL_WORD_TXT} {self.logic.word}")

            return letter_press

    def restart_game(self):
        """ restart the variables and prepare
        everything for a hole new game"""
        self.time.restart_time()
        self.board.restart_board(self.logic)
        self.logic.restart_game(self.board.board)
        self.word_lst.restart_world_lst()
        self.score.update_score(f" {INITIAL_SCORE_TXT} {INITIAL_SCORE}")
        self.guess.update_guess(INITIAL_WORD_TXT)

    def exit(self):
        """exit the game if the user chose so"""
        self.root.destroy()


if __name__ == '__main__':
    words_dict = [word.strip() for word in open(WORD_DICT, 'r')]
    board_lst = randomize_board
    g = Boggle(words_dict, board_lst)
    g.run()
