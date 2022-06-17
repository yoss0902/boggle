from boggle_board_randomizer import *
from copy import deepcopy
import tkinter as tk
from tkinter import messagebox

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


class OuterFrame:
    """a class for the main frame of the game

        attributes:
                root, frame

        methods:
                getters
    """

    def __init__(self, root):
        """a constructor how receive root and
        create the frame upon it"""
        self.__root = root
        self.__outer_frame = tk.Frame(self.root, **OUTER_FRAME_STYLE)
        self.frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    @property
    def root(self):
        """root getter"""
        return self.__root

    @property
    def frame(self):
        """the frame getter """
        return self.__outer_frame


class Board:
    """a class for the board buttons of the game which create the buttons
    and the frame they are seating on
        attributes:
                randomise board function, board, game's main frame, buttons
                buttons's frame, updating variables function
        methods:
                getters and setters,
                create buttons,
                lock and unlock buttons
                restart board
    """

    def __init__(self, frame, updating_variables, board):
        """a constructor how create tha vars necessary for the class"""
        self.__rand_board = board
        self.__board = self.rand_board(LETTERS)
        self.__outer_frame = frame
        self.__buttons = deepcopy(INITIAL_BOARD)
        self.__middle_frame = tk.Frame(self.frame, bg=MIDDLE_FRAME_BG)
        self.board_frame.grid(row=1, column=1, rowspan=3, columnspan=1, sticky=STICK_ALL_DIRECTION)
        self.__updating_variables = updating_variables
        self.create_button_in_middle_frame(INITIAL_BOARD)

    @property
    def rand_board(self):
        """randomize func getter"""
        return self.__rand_board

    @property
    def board(self):
        """board getter"""
        return self.__board

    @board.setter
    def board(self, board):
        """board setter"""
        self.__board = board

    @property
    def frame(self):
        """main frame getter"""
        return self.__outer_frame

    @property
    def buttons(self):
        """buttons getter"""
        return self.__buttons

    @property
    def board_frame(self):
        """board frame getter"""
        return self.__middle_frame

    @property
    def updating(self):
        """updating function getter"""
        return self.__updating_variables

    def create_button_in_middle_frame(self, board):
        """a function how creates the board buttons for the game"""
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.buttons[i][j] = tk.Button(self.board_frame, text=board[i][j], **CUBES_BUTTON_STYLE,
                                               command=self.updating(i, j), state=NORMAL_STATE)
                self.buttons[i][j].grid(row=i, column=j, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)

    def lock_and_unlock_buttons(self, available_cells, word_path):
        """a function who's lock and unlock
        cells according to the last pressed cells"""
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.buttons[i][j]["state"] = DISABLED_STATE
        for k in available_cells:
            row, col = k
            if (row, col) not in word_path:
                self.buttons[row][col].configure(state=NORMAL_STATE)

    def restart_board(self, boggle_logic):
        """a function who's initialize the board when the game starts over """
        self.board = self.rand_board(LETTERS)
        self.create_button_in_middle_frame(self.board)
        self.lock_and_unlock_buttons(boggle_logic.all_cells(), [])


class Timer:
    """a class for the timer

        attributes:
                time flag, second left, main frame, time label, restart func and exit func

        methods:
                getters and setters
                restart time
                run timer
    """

    def __init__(self, frame, restart_game, exit):
        """a constructor who's initialize and creates the vars for the class"""
        self.__time_flag = False
        self.__second_count = 5
        self.__outer_frame = frame
        self.__time_label = tk.Label(self.frame, text=f'{TIME_TXT} {INITIAL_TIME}', **WIDGET_STYLE)
        self.time_label.grid(row=0, column=0, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)
        self.__restart_game = restart_game
        self.__exit = exit
        self.time_label.after(ONE_SEC, self.run_timer)

    @property
    def time_flag(self):
        """time flag getter"""
        return self.__time_flag

    @time_flag.setter
    def time_flag(self, flag):
        """time flag setter"""
        self.__time_flag = flag

    @property
    def second(self):
        """seconds left getters"""
        return self.__second_count

    @second.setter
    def second(self, new_sec):
        """seconds left setters"""
        self.__second_count = new_sec

    @property
    def frame(self):
        """main frame getter"""
        return self.__outer_frame

    @property
    def time_label(self):
        """time label getter"""
        return self.__time_label

    @property
    def restart(self):
        """restart func getter"""
        return self.__restart_game

    @property
    def exit(self):
        """exit func getter"""
        return self.__exit

    def restart_time(self):
        """restart the timer when the gam start over """
        self.time_flag = True
        self.second = THREE_MINUTES_IN_SEC
        self.time_label.config(fg=WIDGET_TXT_COLOR)
        self.time_label.config(text=f"{TIME_TXT} {REINITIAL_TIME}")

    def run_timer(self):
        """ main engine of the timer"""
        if self.time_flag:
            if self.second > -1:
                mins, secs = divmod(self.second, 60)
                mins = "{:02d}".format(mins)
                secs = "{:02d}".format(secs)
                self.time_label.config(text=f"{TIME_TXT} {mins}:{secs}")
                if self.second <= 10:
                    self.time_label.config(fg="OrangeRed3")
                if self.second == 0:
                    self.time_flag = False
                    game_flag = messagebox.askretrycancel(END_GAME_TITLE, END_GAME_MSG)
                    if game_flag:
                        self.restart()
                    else:
                        self.exit()
                self.second -= 1
        self.time_label.after(ONE_SEC, self.run_timer)


class Score:
    def __init__(self, frame):
        self.__outer_frame = frame
        self.__score_label = tk.Label(self.outer_frame, text=INITIAL_SCORE_TXT + INITIAL_SCORE, **WIDGET_STYLE)
        self.score_label.grid(row=1, column=0, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)

    @property
    def outer_frame(self):
        return self.__outer_frame

    @property
    def score_label(self):
        return self.__score_label

    def update_score(self, update):
        self.score_label.config(text=update)


class CurrentGuess:
    def __init__(self, frame):
        self.__outer_frame = frame
        self.__current_guess_label = tk.Label(self.outer_frame, text=INITIAL_WORD_TXT, **WIDGET_STYLE)
        self.guess_label.config(height=2, width=30)
        self.guess_label.grid(row=0, column=1, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)

    @property
    def outer_frame(self):
        return self.__outer_frame

    @property
    def guess_label(self):
        return self.__current_guess_label

    def update_guess(self, update):
        self.guess_label.config(text=update)


class WordLst:
    def __init__(self, frame):
        self.__outer_frame = frame
        self.__word_lst_label = tk.Label(self.outer_frame, text=FOUND_WORD_TXT, **WIDGET_STYLE)
        self.word_lst_label.grid(row=2, column=0, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)
        self.__found_words = tk.Text(self.outer_frame, **FOUND_WORD_STYLE)
        self.found_words.grid(row=3, column=0, rowspan=2, columnspan=1, sticky=STICK_ALL_DIRECTION)

    @property
    def outer_frame(self):
        return self.__outer_frame

    @property
    def word_lst_label(self):
        return self.__word_lst_label

    @property
    def found_words(self):
        return self.__found_words

    def restart_world_lst(self):
        self.found_words.config(state=NORMAL_STATE)
        self.found_words.delete("1.0", tk.END)
        self.found_words.config(state=DISABLED_STATE)

    def update_word_guesses(self, word_lst):
        self.found_words.config(state=NORMAL_STATE)
        self.found_words.insert(tk.END, f"{word_lst[-1]},")
        self.found_words.config(state=DISABLED_STATE)


class StartButton:
    def __init__(self, frame, time, board):
        self.__time = time
        self.__board = board
        self.__outer_frame = frame
        self.__start_button = tk.Button(self.outer_frame, text=INITIAL_START_TXT, **WIDGET_STYLE, command=self.start)
        self.start_button.configure(bg="medium sea green")
        self.start_button.grid(row=0, column=2, rowspan=1, columnspan=1, sticky="ewns")

    @property
    def time(self):
        return self.__time

    @property
    def board(self):
        return self.__board

    @property
    def outer_frame(self):
        return self.__outer_frame

    @property
    def start_button(self):
        return self.__start_button

    def start(self):
        self.start_button.configure(text=DURING_GAME_START_TXT, state=DISABLED_STATE)
        self.time.time_flag = True
        self.board.create_button_in_middle_frame(self.board.board)


class Rules:
    def __init__(self, frame):
        self.__outer_frame = frame
        self.__rules_button = tk.Button(self.outer_frame, text=RULES_TXT, **WIDGET_STYLE, command=self.rules)
        self.rules_button.grid(row=2, column=2, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)

    @property
    def outer_frame(self):
        return self.__outer_frame

    @property
    def rules_button(self):
        return self.__rules_button

    def rules(self):
        messagebox.showinfo(RULES_MESSEGE_TITLE, RULES)


class Submit:
    def __init__(self, frame, time, boggle_logic, word_lst, cuurent_guess, score, board, words):
        self.__words = words
        self.__time = time
        self.__boggle_logic = boggle_logic
        self.__outer_frame = frame
        self.__word_lst = word_lst
        self.__current_guess = cuurent_guess
        self.__score = score
        self.__board = board
        self.__check_button = tk.Button(self.outer_frame, text=SUBMIT_TXT, **WIDGET_STYLE,
                                        command=self.check_complete_word)
        self.check_button.configure(bg="RoyalBlue1")
        self.check_button.grid(row=1, column=2, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)

    @property
    def word_lst(self):
        return self.__word_lst

    @property
    def words(self):
        return self.__words

    @property
    def time(self):
        return self.__time

    @property
    def outer_frame(self):
        return self.__outer_frame

    @property
    def current_guess(self):
        return self.__current_guess

    @property
    def score(self):
        return self.__score

    @property
    def board(self):
        return self.__board

    @property
    def check_button(self):
        return self.__check_button

    @property
    def logic(self):
        return self.__boggle_logic

    def check_complete_word(self):
        self.logic.check_complete_word(self.time.time_flag, self.submit)

    def submit(self, flag):
        if flag:
            self.word_lst.update_word_guesses(self.logic.word_lst)
            self.current_guess.update_guess(CORRECT_MSG)
            self.score.update_score(f" {INITIAL_SCORE_TXT} {self.logic.score}")
            self.board.lock_and_unlock_buttons(self.logic.all_cells(), self.logic.word_path)
        else:
            self.current_guess.update_guess(WRONG_MSG)
            self.board.lock_and_unlock_buttons(self.logic.all_cells(), self.logic.word_path)


class Image:
    def __init__(self, frame):
        self.__outer_frame = frame
        self.__image = tk.PhotoImage(file=BOGGLE_PHOTO)
        self.__photo_label = tk.Label(self.outer_frame, image=self.image)
        self.photo_label.grid(row=3, column=2, rowspan=1, columnspan=1, sticky=STICK_ALL_DIRECTION)

    @property
    def outer_frame(self):
        return self.__outer_frame

    @property
    def image(self):
        return self.__image

    @property
    def photo_label(self):
        return self.__photo_label
