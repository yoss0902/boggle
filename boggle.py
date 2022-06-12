from boggle_board_randomizer import *
from copy import deepcopy
import tkinter as tk
from tkinter import messagebox
from boggle_logic import *

BUTTON_HOVER_COLOR = "gray"
REGULAR_COLOR = "lightgray"
BUTTON_ACTIVE_COLLOR = "slateblue"

CUBES_BUTTON_STYLE = {"font": ("Courier", 30),
                      "borderwidth": 2,
                      "background": "gray35",
                      "relief": "raised",
                      "bg": "IndianRed3",
                      "fg": "black",
                      "activebackground": "snow",
                      "highlightbackground": "black",
                      "height": 3, "width": 8}

WIDGET_STYLE = {"font": ("david", 25),
                "relief": tk.RAISED,
                "bg": "lightgray",
                "fg": "black",
                "highlightbackground": "black",

                "activebackground": "light sky blue",
                "height": 2, "width": 19}
WELCOMING_MESSEGE = "welcome to our boggle game, to begin, please press start"
WELCOMING_MESSEGE_TITLE = "GREEDINS"
INITIAL_TIME_TXT = "time: "
INITIAL_SCORE_TXT = "score: "
SUBMIT_TXT = "submit"
FOUND_WORD_TXT = "found words"
INITIAL_WORD_TXT = "word: "
INITIAL_START_TXT = "start"
DURING_GAME_START_TXT = "game is on"
RULES_TXT = "Boggle game rules"
RULES = " * Words must be at least three letters in length." "\n" " * Each letter must be a horizontal, vertical, or diagonal neighbor of the one before it." "\n"" * No individual letter cube may be used more than once in a word ""\n"
RULES_MESSEGE_TITLE = "boggle game rules"
WORD_DICT = "boggle_dict.txt"
BOGGLE_PHOTO = "boggle_image.png"
CORRECT_MSG = "correct!"
WRONG_MSG = "wrong!"

INITIAL_BOARD = [['*', '*', '*', '*'],
                 ['*', '*', '*', '*'],
                 ['*', '*', '*', '*'],
                 ['*', '*', '*', '*']]

board = [['N', 'I', 'D', 'I'],
         ['O', 'T', 'TC', 'G'],
         ['Q', 'S', 'E', 'Z'],
         ['U', 'QU', 'C', 'T']]

words = ['ESQU', 'ZTC', 'ITS', 'NID', "NOT"]


class BoggleGui:
    def __init__(self):

        self.words = words
        # self.words = [word.strip() for word in open(WORD_DICT, 'r') ]
        self.initial_board = INITIAL_BOARD
        # self.board = randomize_board(LETTERS)
        self.board = board
        self.boggle_logic = BoggleLogic(self.board, self.words)
        self.root = tk.Tk()
        self.root.title("Boggle Game")
        self.outer_frame = tk.Frame(self.root, width=400, height=400, bg="gray35",
                                    highlightbackground=REGULAR_COLOR, highlightthickness=1)
        self.outer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # board
        self.buttons = deepcopy(self.board)
        self.middle_frame = tk.Frame(self.outer_frame, bg="gray35")
        self.middle_frame.grid(row=1, column=1, rowspan=3, columnspan=1)

        # time
        self.time_flag = False
        self.second_count = 20
        self.time_label = tk.Label(self.outer_frame, text=f'{INITIAL_TIME_TXT} 00:00', **WIDGET_STYLE)
        self.time_label.grid(row=0, column=0, rowspan=1, columnspan=1)

        # score
        self.score_label = tk.Label(self.outer_frame, text=INITIAL_SCORE_TXT, **WIDGET_STYLE)
        self.score_label.grid(row=1, column=0, rowspan=1, columnspan=1)

        # current_guess
        self.current_guess_label = tk.Label(self.outer_frame, font=("david", 25), text=INITIAL_WORD_TXT, bg=REGULAR_COLOR,
                                            relief="raised", height=2, width=50)
        self.current_guess_label.grid(row=0, column=1, rowspan=1, columnspan=1)

        # word_list
        self.word_lst_label = tk.Label(self.outer_frame, text=FOUND_WORD_TXT, **WIDGET_STYLE)
        self.word_lst_label.grid(row=2, column=0, rowspan=1, columnspan=1)
        self.found_words = tk.Text(self.outer_frame, font=("Ariel", 20), height=13, width=20, relief="ridge",
                                   bg="lightgray", fg="black", state="disabled")
        self.found_words.grid(row=3, column=0, rowspan=2, columnspan=1)

        # start_butoon
        self.start_button = tk.Button(self.outer_frame, text=INITIAL_START_TXT, **WIDGET_STYLE, command=self.start)
        self.start_button.grid(row=0, column=2, rowspan=1, columnspan=1)

        # rules label
        self.rules_button = tk.Button(self.outer_frame, text=RULES_TXT , **WIDGET_STYLE, command=self.rules)
        self.rules_button.grid(row=2, column=2, rowspan=1, columnspan=1)

        # check word button
        self.check_button = tk.Button(self.outer_frame, text=SUBMIT_TXT, **WIDGET_STYLE,
                                      command=self.check_complete_word)
        self.check_button.grid(row=1, column=2, rowspan=1, columnspan=1)

        self.create_button_in_middle_frame(INITIAL_BOARD)
        messagebox.showinfo(WELCOMING_MESSEGE_TITLE, WELCOMING_MESSEGE)
        self.time_label.after(1000, self.run_timer)

        # photo
        # self.image1 = Image.open(BOGGLE_PHOTO)
        # self.resizes = self.image1.resize((400, 300))
        # self.image = tk.PhotoImage(file = BOGGLE_PHOTO)
        #
        # # self.image.resize((400, 300))
        # self.photo_label = tk.Label(self.outer_frame, image = self.image )
        # self.photo_label.grid(row = 3, column = 2, rowspan=1, columnspan=1)

    def rules(self):
        messagebox.showinfo(RULES_MESSEGE_TITLE, RULES)

    def run(self):
        self.root.mainloop()

    def create_button_in_middle_frame(self, board):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.buttons[i][j] = tk.Button(self.middle_frame, text=board[i][j], **CUBES_BUTTON_STYLE,
                                               command=self.updating_variables(i, j), state="normal")
                self.buttons[i][j].grid(row=i, column=j, rowspan=1, columnspan=1, sticky=tk.NSEW)

    def updating_variables(self, row, col):
        if self.time_flag:
            def letter_press():
                self.boggle_logic.updating_variables(row, col, self.time_flag)
                available_cells = self.boggle_logic.available_cell_to_choose(row, col)
                current_word = self.boggle_logic.word
                word_path = self.boggle_logic.word_path
                self.lock_and_unlock_buttons(available_cells, word_path)
                self.current_guess_label.config(text=f" {INITIAL_WORD_TXT} {current_word}")

            return letter_press

    def lock_and_unlock_buttons(self, available_cells, word_path):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.buttons[i][j]["state"] = "disabled"
        for k in available_cells:
            row, col = k
            if (row, col) not in word_path:
                self.buttons[row][col].configure(state="normal")

    def check_complete_word(self):
        if self.time_flag and len(self.boggle_logic.word) >= 3:
            if self.boggle_logic.word in self.words and self.boggle_logic.word not in self.boggle_logic.word_lst:
                self.boggle_logic.word_lst.append(self.boggle_logic.word)
                self.boggle_logic.score += len(self.boggle_logic.word_path) ** 2
                self.found_words.config(state="normal")
                self.found_words.insert(tk.END, f"{self.boggle_logic.word_lst[-1]},")
                self.found_words.config(state="disabled")
                self.current_guess_label.config(text=CORRECT_MSG )
                self.score_label.config(text=f" {INITIAL_SCORE_TXT} {self.boggle_logic.score}")
                self.boggle_logic.check_complete_word(self.time_flag)
                self.lock_and_unlock_buttons(self.boggle_logic.all_cells(), self.boggle_logic.word_path)
            else:
                self.boggle_logic.check_complete_word(self.time_flag)
                self.current_guess_label.config(text=WRONG_MSG)
                self.lock_and_unlock_buttons(self.boggle_logic.all_cells(), self.boggle_logic.word_path)

    def run_timer(self):
        if self.time_flag:
            if self.second_count > -1:
                mins, secs = divmod(self.second_count, 60)
                self.time_label.config(text=f"{INITIAL_TIME_TXT} {mins}:{secs}")
                if self.second_count == 0:
                    self.time_flag = False
                    game_flag = messagebox.askretrycancel("popup", "game is over! ")
                    if game_flag:
                        self.restart_game()
                    else:
                        self.exit()
                self.second_count -= 1
        self.time_label.after(1000, self.run_timer)

    def start(self):
        self.start_button.configure(text=DURING_GAME_START_TXT, state="disabled")
        self.time_flag = True
        self.create_button_in_middle_frame(self.board)

    def restart_game(self):
        self.boggle_logic.restart_game()
        self.time_flag = True
        # self.board = randomize_board(LETTERS)
        self.board = board
        self.boggle_logic.set_board(self.board)
        self.second_count = 180
        self.create_button_in_middle_frame(self.board)
        self.found_words.config(state="normal")
        self.found_words.delete("1.0", tk.END)
        self.found_words.config(state="disabled")
        self.lock_and_unlock_buttons(self.boggle_logic.all_cells(), [])
        self.score_label.config(text=f" {INITIAL_SCORE_TXT} 0")
        self.current_guess_label.config(text=INITIAL_WORD_TXT)
        self.time_label.config(text=f"{INITIAL_TIME_TXT} 03:00")

    def exit(self):
        self.root.destroy()


g = BoggleGui()
g.run()
