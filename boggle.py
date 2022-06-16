from boggle_board_randomizer import *
from copy import deepcopy
import tkinter as tk
from tkinter import messagebox
from boggle_logic import *

# time
TIME_TXT = "time: "
INITIAL_TIME = "00:00"
REINITIAL_TIME = "03:00"
ONE_SEC = 1000
THREE_MINUTES_IN_SEC = 180

# score
INITIAL_SCORE_TXT = "score: "
INITIAL_SCORE = "0"

# submit
SUBMIT_TXT = "submit"

# current word
INITIAL_WORD_TXT = "word: "

# start
INITIAL_START_TXT = "start"
DURING_GAME_START_TXT = "game is on"

# rules
RULES_TXT = "Boggle game rules"
RULES = " * Words must be at least three letters in length." "\n" \
        " * Each letter must be a horizontal, vertical, or diagonal neighbor of the one before it." "\n " \
        " * No individual letter cube may be used more than once in a word "
RULES_MESSEGE_TITLE = "boggle game rules"

# game
WORD_DICT = "boggle_dict.txt"
BOGGLE_PHOTO = "boggle_image.png"
CORRECT_MSG = "correct!"
WRONG_MSG = "wrong!"
END_GAME_TITLE = "game is over!"
END_GAME_MSG = "would you like to play again? "
GAME_TITLE = "Let's play Boggle!"
NORMAL_STATE = "normal"
DISABLED_STATE = "disabled"
STICK_ALL_DIRECTION = "nsew"

# cubes button
INITIAL_BOARD = [["*" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
MIDDLE_FRAME_BG = "gray35"
CUBES_BUTTON_FONT = "Courier"
CUBES_BUTTON_FONT_SIZE = 25
CUBES_BUTTON_FONT_COLOR = "black"
CUBES_BUTTON_BORDERWIDTH_SIZE = 2
CUBES_BUTTON_BACKGROUND_COLOR = "LightCoral"
CUBES_BUTTON_HEIGHT = 3
CUBES_BUTTON_WIDTH = 7
CUBES_BUTTON_ACTIVE_COLOR = "snow"
CUBES_BUTTON_RELIEF = "raised"

CUBES_BUTTON_STYLE = {"font": (CUBES_BUTTON_FONT, CUBES_BUTTON_FONT_SIZE),
                      "borderwidth": CUBES_BUTTON_BORDERWIDTH_SIZE,
                      "relief": CUBES_BUTTON_RELIEF,
                      "bg": CUBES_BUTTON_BACKGROUND_COLOR,
                      "fg": CUBES_BUTTON_FONT_COLOR,
                      "activebackground": CUBES_BUTTON_ACTIVE_COLOR,
                      "highlightbackground": CUBES_BUTTON_FONT_COLOR,
                      "height": CUBES_BUTTON_HEIGHT,
                      "width": CUBES_BUTTON_WIDTH}

# widgets
WIDGET_TXT_FONT = "david"
WIDGET_TXT_SIZE = 25
WIDGET_BACKGROUND = "tan2"
WIDGET_RELIEF = "raised"
WIDGET_TXT_COLOR = "black"
WIDGET_ACTIVE_COLOR = "light sky blue"
WIDGET_HEIGHT = 2
WIDGET_WIDTH = 17

WIDGET_STYLE = {"font": (WIDGET_TXT_FONT, WIDGET_TXT_SIZE),
                "relief": WIDGET_RELIEF,
                "bg": WIDGET_BACKGROUND,
                "fg": WIDGET_TXT_COLOR,
                "activebackground": WIDGET_ACTIVE_COLOR,
                "height": WIDGET_HEIGHT,
                "width": WIDGET_WIDTH}

# outer frame
OUTER_FRAME_WIDTH = 400
OUTER_FRAME_HEIGHT = 400
OUTER_FRAME_BG = "gray35"
OUTER_FRAME_HIGHLIGHTBG = "lightgray"
OUTER_FRAME_HIGHLIGHT_THICK = 1

OUTER_FRAME_STYLE = {"width": OUTER_FRAME_WIDTH,
                     "height": OUTER_FRAME_HEIGHT,
                     "bg": OUTER_FRAME_BG,
                     "highlightbackground": OUTER_FRAME_HIGHLIGHTBG,
                     "highlightthickness": OUTER_FRAME_HIGHLIGHT_THICK}

# found words
FOUND_WORD_TXT = "found words"
FOUND_WORD_FONT = "Ariel"
FOUND_WORD_FONT_SIZE = 20
FOUND_WORD_HEIGHT = 10
FOUND_WORD_WIDTH = 20
FOUND_WORD_RELIEF = "ridge"
FOUND_WORD_BG = "lightgray"
FOUND_WORD_FG = "black"

FOUND_WORD_STYLE = {"state": DISABLED_STATE,
                    "font": (FOUND_WORD_FONT, FOUND_WORD_FONT_SIZE),
                    "height": FOUND_WORD_HEIGHT,
                    "width": FOUND_WORD_WIDTH,
                    "relief": FOUND_WORD_RELIEF,
                    "bg": FOUND_WORD_BG,
                    "fg": FOUND_WORD_FG}


class BoggleGui:
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
        """ the GUI constructor which create the widget of the game"""
        self.__words = words
        self.__root = tk.Tk()
        self.get_root().title(GAME_TITLE)
        self.__outer_frame = OuterFrame(self.get_root())
        self.__time = Timer(self.get_frame().get_frame(), self.restart_game, self.exit)
        self.__board = Board(self.get_frame().get_frame(), self.updating_variables, board)
        self.__boggle_logic = BoggleLogic(self.get_board().get_board(), self.get_words())
        self.__score = Score(self.get_frame().get_frame())
        self.__current_guess = CurrentGuess(self.get_frame().get_frame())
        self.__word_lst = WordLst(self.get_frame().get_frame())
        self.start_button = StartButton(self.get_frame().get_frame(), self.get_time(), self.get_board())
        self.rules = Rules(self.get_frame().get_frame())
        self.submit = Submit(self.get_frame().get_frame(), self.get_time(), self.get_logic(), self.word_lst,
                             self.get_guess(), self.get_score(), self.get_board(), self.get_words())
        self.image = Image(self.get_frame().get_frame())

    def get_words(self):
        return self.__words

    def get_root(self):
        return self.__root

    def get_frame(self):
        return self.__outer_frame

    def get_time(self):
        return self.__time

    def get_board(self):
        return self.__board

    def get_logic(self):
        return self.__boggle_logic

    def get_score(self):
        return self.__score

    def get_guess(self):
        return self.__current_guess

    @property
    def word_lst(self):
        return self.__word_lst

    def run(self):
        """run the mainloop of the GUI"""
        self.get_root().mainloop()

    def updating_variables(self, row, col):
        """ updating the variable each time a board
        button have been pressed"""
        if self.get_time().time_flag:
            def letter_press():
                self.get_logic().updating_variables(row, col, self.get_time().time_flag)
                available_cells = self.get_logic().available_cell_to_choose(row, col)
                current_word = self.get_logic().word
                word_path = self.get_logic().word_path
                self.get_board().lock_and_unlock_buttons(available_cells, word_path)
                self.get_guess().current_guess_label.config(text=f" {INITIAL_WORD_TXT} {current_word}")

            return letter_press

    def restart_game(self):
        """ restart the variables and prepare
        everything for a hole new game"""
        self.get_time().restart_time()
        self.get_board().restart_board(self.get_logic())
        self.get_logic().restart_game(self.get_board().get_board())
        self.word_lst.restart_world_lst()
        self.get_score().restart_score()
        self.get_guess().restart_guess()

    def exit(self):
        """exit the game if the user chose so"""
        self.get_root().destroy()


class OuterFrame:
    def __init__(self, root):
        self.__root = root
        self.__outer_frame = tk.Frame(self.get_root(), **OUTER_FRAME_STYLE)
        self.get_frame().pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    def get_root(self):
        return self.__root

    def get_frame(self):
        return self.__outer_frame


class Board:
    """a class for the board buttons of the game which create the buttons
    and the frame they are seating on"""

    def __init__(self, frame, updating_variables, board):
        self.__board = board
        self.__outer_frame = frame
        self.__buttons = deepcopy(self.get_board())
        self.__middle_frame = tk.Frame(self.get_frame(), bg=MIDDLE_FRAME_BG)
        self.get_board_frame().grid(row=1, column=1, rowspan=3, columnspan=1, sticky=STICK_ALL_DIRECTION)
        self.__updating_variables = updating_variables
        self.create_button_in_middle_frame(INITIAL_BOARD)

    def get_board(self):
        return self.__board

    def set_board(self, board):
        if type(board) == list:
            self.__board = board

    def get_frame(self):
        return self.__outer_frame

    def get_buttons(self):
        return self.__buttons

    def get_board_frame(self):
        return self.__middle_frame

    def get_updating_func(self):
        return self.__updating_variables

    def create_button_in_middle_frame(self, board):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.get_buttons()[i][j] = tk.Button(self.get_board_frame(), text=board[i][j], **CUBES_BUTTON_STYLE,
                                                     command=self.get_updating_func()(i, j), state=NORMAL_STATE)
                self.get_buttons()[i][j].grid(row=i, column=j, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)

    def lock_and_unlock_buttons(self, available_cells, word_path):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.get_buttons()[i][j]["state"] = DISABLED_STATE
        for k in available_cells:
            row, col = k
            if (row, col) not in word_path:
                self.get_buttons()[row][col].configure(state=NORMAL_STATE)

    def restart_board(self, boggle_logic):
        self.set_board(randomize_board(LETTERS))
        self.create_button_in_middle_frame(self.get_board())
        self.lock_and_unlock_buttons(boggle_logic.all_cells(), [])


class Timer:

    def __init__(self, frame, restart_game, exit):
        self.__time_flag = False
        self.__second_count = 2
        self.__outer_frame = frame
        self.__time_label = tk.Label(self.get_frame(), text=f'{TIME_TXT} {INITIAL_TIME}', **WIDGET_STYLE)
        self.get_time_label().grid(row=0, column=0, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)
        self.__restart_game = restart_game
        self.__exit = exit
        self.get_time_label().after(ONE_SEC, self.run_timer)

    @property
    def time_flag(self):
        return self.__time_flag

    @time_flag.setter
    def time_flag(self, flag):
        self.__time_flag = flag

    def get_second(self):
        return self.__second_count

    def set_second(self, new_sec):
        self.__second_count = new_sec

    def get_frame(self):
        return self.__outer_frame

    def get_time_label(self):
        return self.__time_label

    def get_restart(self):
        return self.__restart_game

    def get_exit(self):
        return self.__exit

    def restart_time(self):
        self.time_flag = True
        self.set_second(THREE_MINUTES_IN_SEC)
        self.get_time_label().config(fg=WIDGET_TXT_COLOR)
        self.get_time_label().config(text=f"{TIME_TXT} {REINITIAL_TIME}")

    def run_timer(self):
        if self.time_flag:
            if self.get_second() > -1:
                mins, secs = divmod(self.get_second(), 60)
                mins = "{:02d}".format(mins)
                secs = "{:02d}".format(secs)
                self.get_time_label().config(text=f"{TIME_TXT} {mins}:{secs}")
                if self.get_second() <= 10:
                    self.get_time_label().config(fg="OrangeRed3")
                if self.get_second() == 0:
                    self.time_flag = False
                    game_flag = messagebox.askretrycancel(END_GAME_TITLE, END_GAME_MSG)
                    if game_flag:
                        self.get_restart()()
                    else:
                        self.get_exit()()
                self.set_second(self.get_second() - 1)
        self.get_time_label().after(ONE_SEC, self.run_timer)


class Score:
    def __init__(self, frame):
        self.outer_frame = frame
        self.score_label = tk.Label(self.outer_frame, text=INITIAL_SCORE_TXT + INITIAL_SCORE, **WIDGET_STYLE)
        self.score_label.grid(row=1, column=0, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)

    def restart_score(self):
        self.score_label.config(text=f" {INITIAL_SCORE_TXT} {INITIAL_SCORE}")


class CurrentGuess:
    def __init__(self, frame):
        self.outer_frame = frame
        self.current_guess_label = tk.Label(self.outer_frame, text=INITIAL_WORD_TXT, **WIDGET_STYLE)
        self.current_guess_label.config(height=2, width=30)
        self.current_guess_label.grid(row=0, column=1, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)

    def update_guess(self, update):
        self.current_guess_label.config(text=update)

    def restart_guess(self):
        self.current_guess_label.config(text=INITIAL_WORD_TXT)


class WordLst:
    def __init__(self, frame):
        self.outer_frame = frame
        self.word_lst_label = tk.Label(self.outer_frame, text=FOUND_WORD_TXT, **WIDGET_STYLE)
        self.word_lst_label.grid(row=2, column=0, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)
        self.found_words = tk.Text(self.outer_frame, **FOUND_WORD_STYLE)
        self.found_words.grid(row=3, column=0, rowspan=2, columnspan=1, sticky=STICK_ALL_DIRECTION)

    def restart_world_lst(self):
        self.found_words.config(state=NORMAL_STATE)
        self.found_words.delete("1.0", tk.END)
        self.found_words.config(state=DISABLED_STATE)

    def update_word_guesses(self, game_logic):
        self.found_words.config(state=NORMAL_STATE)
        self.found_words.insert(tk.END, f"{game_logic.word_lst[-1]},")
        self.found_words.config(state=DISABLED_STATE)


class StartButton:
    def __init__(self, frame, time, board):
        self.time = time
        self.board = board
        self.outer_frame = frame
        self.start_button = tk.Button(self.outer_frame, text=INITIAL_START_TXT, **WIDGET_STYLE, command=self.start)
        self.start_button.configure(bg="medium sea green")
        self.start_button.grid(row=0, column=2, rowspan=1, columnspan=1, sticky="ewns")

    def start(self):
        self.start_button.configure(text=DURING_GAME_START_TXT, state=DISABLED_STATE)
        self.time.time_flag = True
        self.board.create_button_in_middle_frame(self.board.get_board())


class Rules:
    def __init__(self, frame):
        self.outer_frame = frame
        self.rules_button = tk.Button(self.outer_frame, text=RULES_TXT, **WIDGET_STYLE, command=self.rules)
        self.rules_button.grid(row=2, column=2, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)

    def rules(self):
        messagebox.showinfo(RULES_MESSEGE_TITLE, RULES)


class Submit:
    def __init__(self, frame, time, boggle_logic, word_lst, cuurent_guess, score, board, words):
        self.words = words
        self.time = time
        self.__boggle_logic = boggle_logic
        self.outer_frame = frame
        self.word_lst = word_lst
        self.current_guess = cuurent_guess
        self.score = score
        self.board = board
        self.check_button = tk.Button(self.outer_frame, text=SUBMIT_TXT, **WIDGET_STYLE,
                                      command=self.check_complete_word)
        self.check_button.configure(bg="RoyalBlue1")
        self.check_button.grid(row=1, column=2, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)

    def get_logic(self):
        return self.__boggle_logic

    def check_complete_word(self):
        if self.time.time_flag and len(self.get_logic().word) >= 3:
            if self.get_logic().word in self.words and self.get_logic().word not in self.get_logic().word_lst:
                self.get_logic().word_lst.append(self.get_logic().word)
                self.get_logic().score += len(self.get_logic().word_path) ** 2

                self.word_lst.update_word_guesses(self.get_logic())
                self.current_guess.update_guess(CORRECT_MSG)
                # self.current_guess.current_guess_label.config(text=CORRECT_MSG)
                self.score.score_label.config(text=f" {INITIAL_SCORE_TXT} {self.get_logic().score}")

                self.get_logic().check_complete_word(self.time.time_flag)

                self.board.lock_and_unlock_buttons(self.get_logic().all_cells(), self.get_logic().word_path)
            else:
                self.get_logic().check_complete_word(self.time.time_flag)
                self.current_guess.update_guess(WRONG_MSG)
                # self.current_guess.current_guess_label.config(text=WRONG_MSG)
                self.board.lock_and_unlock_buttons(self.get_logic().all_cells(), self.get_logic().word_path)


class Image:
    def __init__(self, frame):
        self.outer_frame = frame
        self.image = tk.PhotoImage(file=BOGGLE_PHOTO)
        self.photo_label = tk.Label(self.outer_frame, image=self.image)
        self.photo_label.grid(row=3, column=2, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)


if __name__ == '__main__':
    words_dict = [word.strip() for word in open(WORD_DICT, 'r')]
    board_lst = randomize_board(LETTERS)
    g = BoggleGui(words_dict, board_lst)
    g.run()
