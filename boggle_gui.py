import tkinter as tk
from boggle_board_randomizer import *
import time
from tkinter import messagebox

BUTTON_HOVER_COLOR = "gray"
REGULAR_COLOR = "lightgray"
BUTTON_ACTIVE_COLLOR = "slateblue"
CUBES_BUTTON_STYLE = {"font": ("Courier", 30),
                      "borderwidth": 1,
                      "relief": tk.RAISED,
                      "bg": REGULAR_COLOR,
                      "activebackground": BUTTON_ACTIVE_COLLOR,
                      "height":3, "width":6}


class Timer:
    def __init__(self, frame, root):
        self.root = root
        self.outer_frame = frame
        self.minute_str = tk.StringVar()
        self.second_str = tk.StringVar()
        self.minute_str.set("03")
        self.second_str.set("00")
        self.time_label = tk.Label(self.outer_frame, font=("david", 30),
                                   text=f"time : {self.minute_str.get()} : {self.second_str.get()} ",
                                   bg=REGULAR_COLOR,
                                   relief="ridge")
        self.time_label.grid(row=0, column=0, rowspan=1, columnspan=1)

    # def get_minutes(self):
    #     return self.minute_str
    #
    # def get_seconds(self):
    #     return self.second_str

    def run_timer(self):
        second_count = int(self.minute_str.get() * 60) + int(self.second_str.get())
        while second_count > -1:
            mins, secs = divmod(second_count, 60)
            self.minute_str.set("{0:2d}".format(mins))
            self.second_str.set("{0:2d}".format(secs))
            self.outer_frame.update()
            time.sleep(1)
            if second_count == 0:
                messagebox.showinfo("pay attention", "game is over")
            second_count -= 1


class Score:
    def __init__(self, frame):
        self.outer_frame = frame

        self.score_label = tk.Label(self.outer_frame, text=f"score: ", font=("david", 30),
                                    bg=REGULAR_COLOR, width=15, relief="ridge")
        self.score_label.grid(row=1, column=0, rowspan=1, columnspan=1)


class CubesBoard:

    def __init__(self, frame, board):
        self.outer_frame = frame
        self.__board = board
        self.buttons = {}
        self.__middle_frame = tk.Frame(self.outer_frame)
        self.__middle_frame.grid(row=1, column=1, rowspan=2, columnspan=1)

    def get_middle_frame(self):
        return self.__middle_frame

    def get_board(self):
        return self.__board

    # def set_board(self):
    #     self.board = randomize_board(LETTERS)

    def create_button_in_middle_frame(self):
        for i in range(BOARD_SIZE):
            tk.Grid.columnconfigure(self.get_middle_frame(), i, weight=1)
        for j in range(BOARD_SIZE):
            tk.Grid.rowconfigure(self.get_middle_frame(), j, weight=1)
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.make_button(self.get_board()[i][j], i, j)

    def make_button(self, button_char, row, col, rowspan=1, columnspan=1):
        button = tk.Button(self.get_middle_frame(), text=button_char, **CUBES_BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tk.NSEW)
        self.buttons[button_char] = button


class CurrentGuess:
    def __init__(self, frame):
        self.outer_frame = frame
        self.current_guess_label = tk.Label(self.outer_frame, font=("david", 30), text="word var", bg=REGULAR_COLOR,
                                            width=15, relief="ridge")
        self.current_guess_label.grid(row=0, column=1, rowspan=1, columnspan=1)


class GuessedWords:
    def __init__(self, frame):
        self.outer_frame = frame
        self.word_list = []
        self.word_lst_to_print = tk.StringVar(self.word_list)
        self.found_words = tk.Label(self.outer_frame, text="word_lst", font=("Ariel", 20), width=10, relief="ridge")
        self.found_words.grid(row=2, column=0, rowspan=1, columnspan=1)

    def update_word_lst(self):
        ...


class StartButton:

    def __init__(self, frame, timer):
        self.outer_frame = frame
        self.start = self.start()
        self.start_button = tk.Button(self.outer_frame, text="start", bg="blue", font=("david", 20), width=10,
                                      relief="ridge", command = timer.run_timer)
        self.start_button.grid(row=0, column=2, rowspan=1, columnspan=1)

    def start(self):
        """ initialize a game and change button text and color"""
        ...


class BoggleGui:

    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Boggle Game")
        self.__outer_frame = tk.Frame(self.root, width=400, height=400, bg=REGULAR_COLOR,
                                      highlightbackground=REGULAR_COLOR,
                                      highlightthickness=5)
        self.__outer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.__cubes_board = CubesBoard(self.get_outer_frame(), randomize_board(LETTERS))
        self.__timer = Timer(self.get_outer_frame(), self.root)
        self.__score = Score(self.get_outer_frame())
        self.__guessed_word = GuessedWords(self.get_outer_frame())
        self.__current_word = CurrentGuess(self.get_outer_frame())
        self.start = StartButton(self.get_outer_frame(), self.get_timer())

        self.__instruction_lable = tk.Label(self.get_outer_frame(), text="game instruction", font=("Ariel", 15),
                                            bg="yellow", relief="ridge")
        self.__instruction_lable.grid(row=1, column=2, rowspan=2, columnspan=1)
        self.__cubes_board.create_button_in_middle_frame()

    # def get_root(self):
    #     return self.__root

    def get_outer_frame(self):
        return self.__outer_frame

    def get_cubes_board(self):
        return self.__cubes_board

    def get_timer(self):
        return self.__timer

    def get_score(self):
        return self.__score

    def get_guessed_word(self):
        return self.__guessed_word

    def get_current_word(self):
        return self.__guessed_word

    def run(self):
        self.root.mainloop()


board = randomize_board(LETTERS)
# print(board)
g = BoggleGui()
g.run()
