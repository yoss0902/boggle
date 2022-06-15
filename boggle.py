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
        " * Each letter must be a horizontal, vertical, or diagonal neighbor of the one before it." "\n "\
        " * No individual letter cube may be used more than once in a word "
RULES_MESSEGE_TITLE = "boggle game rules"

# game
WORD_DICT = "boggle_dict.txt"
BOGGLE_PHOTO = "boggle_image.png"
CORRECT_MSG = "correct!"
WRONG_MSG = "wrong!"
END_GAME_TITLE = "game is over!"
END_GAME_MSG = "would you like to play again? "
GAME_TITLE = "Boggle Game"
NORMAL_STATE = "normal"
DISABLED_STATE = "disabled"

# BUTTON_COLOR = "gray"
REGULAR_COLOR = "lightgray"

# cubes button
MIDDLE_FRAME_BG = "gray35"
CUBES_BUTTON_FONT = "Courier"
CUBES_BUTTON_FONT_SIZE = 25
CUBES_BUTTON_FONT_COLOR = "black"
CUBES_BUTTON_BORDERWIDTH_SIZE = 2
CUBES_BUTTON_BACKGROUND_COLOR = "IndianRed3"
CUBES_BUTTON_HEIGHT = 3
CUBES_BUTTON_WIDTH = 7
CUBES_BUTTON_ACTIVE_COLOR = "snow"
CUBES_BUTTON_RELIEF = "raised"

CUBES_BUTTON_STYLE = {"font": (CUBES_BUTTON_FONT, CUBES_BUTTON_FONT_SIZE),
                      "borderwidth": CUBES_BUTTON_BORDERWIDTH_SIZE,
                      "relief":CUBES_BUTTON_RELIEF,
                      "bg": CUBES_BUTTON_BACKGROUND_COLOR,
                      "fg": CUBES_BUTTON_FONT_COLOR,
                      "activebackground": CUBES_BUTTON_ACTIVE_COLOR ,
                      "highlightbackground": CUBES_BUTTON_FONT_COLOR,
                      "height": CUBES_BUTTON_HEIGHT,
                      "width": CUBES_BUTTON_WIDTH}

# widgets
WIDGET_TXT_FONT = "david"
WIDGET_TXT_SIZE = 25
WIDGET_BACKGROUND = "lightgray"
WIDGET_RELIEF = "raised"
WIDGET_TXT_COLOR = "black"
WIDGET_ACTIVE_COLOR = "light sky blue"
WIDGET_HEIGHT = 2
WIDGET_WIDTH = 19

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

OUTER_FRAME_STYLE = {"width":OUTER_FRAME_WIDTH,
                     "height":OUTER_FRAME_HEIGHT,
                     "bg":OUTER_FRAME_BG,
                     "highlightbackground":OUTER_FRAME_HIGHLIGHTBG,
                     "highlightthickness":OUTER_FRAME_HIGHLIGHT_THICK}


# found words
FOUND_WORD_TXT = "found words"
FOUND_WORD_FONT = "Ariel"
FOUND_WORD_FONT_SIZE = 20
FOUND_WORD_HEIGHT = 10
FOUND_WORD_WIDTH = 20
FOUND_WORD_RELIEF = "ridge"
FOUND_WORD_BG = "lightgray"
FOUND_WORD_FG = "black"

FOUND_WORD_STYLE = {"state":DISABLED_STATE,
                    "font":(FOUND_WORD_FONT, FOUND_WORD_FONT_SIZE),
                    "height":FOUND_WORD_HEIGHT,
                    "width":FOUND_WORD_WIDTH,
                    "relief":FOUND_WORD_RELIEF,
                    "bg":FOUND_WORD_BG,
                    "fg":FOUND_WORD_FG}


class BoggleGui:
    def __init__(self):
        self.words = [word.strip() for word in open(WORD_DICT, 'r') ]
        self.root = tk.Tk()
        self.root.title(GAME_TITLE)
        self.outer_frame = tk.Frame(self.root, **OUTER_FRAME_STYLE)
        self.outer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.time = Timer(self.outer_frame, self.restart_game, self.exit)
        self.board = Board(self.outer_frame, self.time.time_flag, self.updating_variables)
        self.boggle_logic = BoggleLogic(self.board.board, self.words)
        self.score = Score(self.outer_frame)
        self.current_guess = CurrentGuess(self.outer_frame)
        self.word_lst = WordLst(self.outer_frame)
        self.start_button = StartButton(self.outer_frame, self.time, self.board)
        self.rules = Rules(self.outer_frame)
        self.submit = Submit(self.outer_frame, self.time, self.boggle_logic, self.word_lst, self.current_guess,
                             self.score, self.board, self.words)
        self.image = Image(self.outer_frame)

    def run(self):
        self.root.mainloop()

    def updating_variables(self, row, col):
        if self.time.time_flag:
            def letter_press():
                self.boggle_logic.updating_variables(row, col, self.time.time_flag)
                available_cells = self.boggle_logic.available_cell_to_choose(row, col)
                current_word = self.boggle_logic.word
                word_path = self.boggle_logic.word_path
                self.board.lock_and_unlock_buttons(available_cells, word_path)
                self.current_guess.current_guess_label.config(text=f" {INITIAL_WORD_TXT} {current_word}")

            return letter_press

    def restart_game(self):
        self.boggle_logic.restart_game()
        self.time.time_flag = True
        self.board.board = randomize_board(LETTERS)
        self.boggle_logic.set_board(self.board.board)
        self.time.second_count = THREE_MINUTES_IN_SEC
        self.board.create_button_in_middle_frame(self.board.board)
        self.word_lst.found_words.config(state=NORMAL_STATE)
        self.word_lst.found_words.delete("1.0", tk.END)
        self.word_lst.found_words.config(state=DISABLED_STATE)
        self.board.lock_and_unlock_buttons(self.boggle_logic.all_cells(), [])
        self.score.score_label.config(text=f" {INITIAL_SCORE_TXT} {INITIAL_SCORE}")
        self.current_guess.current_guess_label.config(text=INITIAL_WORD_TXT)
        self.time.time_label.config(text=f"{TIME_TXT} {REINITIAL_TIME}")

    def exit(self):
        self.root.destroy()

class Board:
    def __init__(self, frame, time_flag, updating_variebles):
        self.initial_board = [["*" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.board = randomize_board(LETTERS)
        self.outer_frame = frame
        self.buttons = deepcopy(self.board)
        self.middle_frame = tk.Frame(self.outer_frame, bg=MIDDLE_FRAME_BG)
        self.middle_frame.grid(row=1, column=1, rowspan=3, columnspan=1, sticky = "nsew")
        self.time_flag = time_flag
        self.updating_variables = updating_variebles
        self.create_button_in_middle_frame(self.initial_board)

    def create_button_in_middle_frame(self, board):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.buttons[i][j] = tk.Button(self.middle_frame, text=board[i][j], **CUBES_BUTTON_STYLE,
                                               command=self.updating_variables(i, j), state=NORMAL_STATE)
                self.buttons[i][j].grid(row=i, column=j, rowspan=1, columnspan=1, sticky=tk.NSEW)

    def lock_and_unlock_buttons(self, available_cells, word_path):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.buttons[i][j]["state"] = DISABLED_STATE
        for k in available_cells:
            row, col = k
            if (row, col) not in word_path:
                self.buttons[row][col].configure(state=NORMAL_STATE)


class Timer:
    def __init__(self,frame, restart_game, exit):
        self.time_flag = False
        self.second_count = 179
        self.outer_frame = frame
        self.time_label = tk.Label(self.outer_frame, text=f'{TIME_TXT} {INITIAL_TIME}', **WIDGET_STYLE)
        self.time_label.grid(row=0, column=0, rowspan=1, columnspan=1, sticky = "nsew")
        self.restart_game = restart_game
        self.exit = exit
        self.time_label.after(ONE_SEC, self.run_timer)

    def run_timer(self):
        if self.time_flag:
            if self.second_count > -1:
                mins, secs = divmod(self.second_count, 60)
                mins = "{:02d}".format(mins)
                secs = "{:02d}".format(secs)
                self.time_label.config(text=f"{TIME_TXT} {mins}:{secs}")
                if self.second_count == 0:
                    self.time_flag = False
                    game_flag = messagebox.askretrycancel(END_GAME_TITLE, END_GAME_MSG)
                    if game_flag:
                        self.restart_game()
                    else:
                        self.exit()
                self.second_count -= 1
        self.time_label.after(ONE_SEC, self.run_timer)


class Score:
    def __init__(self, frame):
        self.outer_frame = frame
        self.score_label = tk.Label(self.outer_frame, text=INITIAL_SCORE_TXT + INITIAL_SCORE, **WIDGET_STYLE)
        self.score_label.grid(row=1, column=0, rowspan=1, columnspan=1, sticky="nsew")


class CurrentGuess:
    def __init__(self, frame):
        self.outer_frame = frame
        self.current_guess_label = tk.Label(self.outer_frame, text=INITIAL_WORD_TXT, **WIDGET_STYLE)
        self.current_guess_label.config(height=2, width=30)
        self.current_guess_label.grid(row=0, column=1, rowspan=1, columnspan=1, sticky="nsew")



class WordLst:
    def __init__(self, frame):
        self.outer_frame = frame
        self.word_lst_label = tk.Label(self.outer_frame, text=FOUND_WORD_TXT, **WIDGET_STYLE)
        self.word_lst_label.grid(row=2, column=0, rowspan=1, columnspan=1, sticky="nsew")
        self.found_words = tk.Text(self.outer_frame, **FOUND_WORD_STYLE)
        self.found_words.grid(row=3, column=0, rowspan=2, columnspan=1, sticky="nsew")


class StartButton:
    def __init__(self, frame, time, board):
        self.time = time
        self.board = board
        self.outer_frame = frame
        self.start_button = tk.Button(self.outer_frame, text=INITIAL_START_TXT, **WIDGET_STYLE, command=self.start)
        self.start_button.grid(row=0, column=2, rowspan=1, columnspan=1, sticky="ewns")


    def start(self):
        self.start_button.configure(text=DURING_GAME_START_TXT, state=DISABLED_STATE)
        self.time.time_flag = True
        self.board.create_button_in_middle_frame(self.board.board)


class Rules:
    def __init__(self,frame):
        self.outer_frame = frame
        self.rules_button = tk.Button(self.outer_frame, text=RULES_TXT , **WIDGET_STYLE, command=self.rules)
        self.rules_button.grid(row=2, column=2, rowspan=1, columnspan=1, sticky = "nsew")



    def rules(self):
        messagebox.showinfo(RULES_MESSEGE_TITLE, RULES)


class Submit:
    def __init__(self, frame, time, boggle_logic, word_lst, cuurent_guess, score, board, words):
        self.words = words
        self.time = time
        self.boggle_logic = boggle_logic
        self.outer_frame = frame
        self.word_lst = word_lst
        self.current_guess = cuurent_guess
        self.score = score
        self.board = board
        self.check_button = tk.Button(self.outer_frame, text=SUBMIT_TXT, **WIDGET_STYLE,
                                      command=self.check_complete_word)
        self.check_button.grid(row=1, column=2, rowspan=1, columnspan=1, sticky="nsew")

    def check_complete_word(self):
        if self.time.time_flag and len(self.boggle_logic.word) >= 3:
            if self.boggle_logic.word in self.words and self.boggle_logic.word not in self.boggle_logic.word_lst:
                self.boggle_logic.word_lst.append(self.boggle_logic.word)
                self.boggle_logic.score += len(self.boggle_logic.word_path) ** 2
                self.word_lst.found_words.config(state=NORMAL_STATE)
                self.word_lst.found_words.insert(tk.END, f"{self.boggle_logic.word_lst[-1]},")
                self.word_lst.found_words.config(state=DISABLED_STATE)
                self.current_guess.current_guess_label.config(text=CORRECT_MSG )
                self.score.score_label.config(text=f" {INITIAL_SCORE_TXT} {self.boggle_logic.score}")
                self.boggle_logic.check_complete_word(self.time.time_flag)
                self.board.lock_and_unlock_buttons(self.boggle_logic.all_cells(), self.boggle_logic.word_path)
            else:
                self.boggle_logic.check_complete_word(self.time.time_flag)
                self.current_guess.current_guess_label.config(text=WRONG_MSG)
                self.board.lock_and_unlock_buttons(self.boggle_logic.all_cells(), self.boggle_logic.word_path)

class Image:
    def __init__(self, frame):
        self.outer_frame = frame
        self.image = tk.PhotoImage(file = BOGGLE_PHOTO)
        self.photo_label = tk.Label(self.outer_frame, image = self.image )
        self.photo_label.grid(row = 3, column = 2, rowspan=1, columnspan=1, sticky = "nsew")


g = BoggleGui()
g.run()
