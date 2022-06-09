import tkinter as tk
from boggle_board_randomizer import *
import time

BUTTON_HOVER_COLOR = "gray"
REGULAR_COLOR = "lightgray"
BUTTON_ACTIVE_COLLOR = "slateblue"
CUBES_BUTTON_STYLE = {"font": ("Courier", 30),
                      "borderwidth": 1,
                      "relief": tk.RAISED,
                      "bg": REGULAR_COLOR,
                      "activebackground": BUTTON_ACTIVE_COLLOR}


class BoggleGui:

    def __init__(self, board):
        self._buttons = {}
        self.root = tk.Tk()
        self.root.title("Boggle Game")
        self.minute = tk.StringVar()
        self.second = tk.StringVar()
        self.minute.set("00")
        self.second.set("03")
        self.board = board
        # self.time_var = tk.StringVar(0)
        self.score_var = tk.StringVar(00)
        self.main_window = self.root
        self.outer_frame = tk.Frame(self.root, width=400, height=400, bg=REGULAR_COLOR,
                                    highlightbackground=REGULAR_COLOR,
                                    highlightthickness=5)
        self.outer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # self.outer_frame.grid(column=800, row=600)
        # self.outer_frame.geometry('800x600')
        self.top_frame = tk.Frame(self.outer_frame)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.score_label = tk.Label(self.top_frame, text=f"score: {self.score_var.get()}", font=("david", 30),
                                    bg=REGULAR_COLOR, width=15, relief="ridge")
        self.score_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.time_label = tk.Label(self.top_frame, font=("david", 30), text = f"time : {self.minute.get()}: {self.second.get()}",
                                   bg=REGULAR_COLOR, width=15, relief="ridge")
        self.time_label.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.right_frame = tk.Frame(self.outer_frame)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.instruction_lable = tk.Label(self.right_frame, text="game instruction", font=("Ariel", 15), bg="yellow",
                                          width=10, relief="ridge")

        self.instruction_lable.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.start_button = tk.Button(self.right_frame, text="start", bg="blue", font=("david", 20), width=10,
                                      relief="ridge", command = self.timer)
        self.start_button.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.left_frame = tk.Frame(self.outer_frame)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH)
        self.found_words = tk.Label(self.left_frame, text="word_lst", font=("Ariel", 20), width=10, relief="ridge")
        self.found_words.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.middle_frame = tk.Frame(self.outer_frame)
        self.middle_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.create_button_in_middle_frame()
        # self.timer()
    # def srart(self):
    #     ...


        self.temp = int(self.minute.get()) * 60 + int(self.second.get())
    def timer(self):
        while self.temp > -1:
            mins, secs = divmod(self.temp, 60)
            print(mins)
            print(secs)
            self.minute.set(mins)
            self.second.set(secs)
            self.root.after(1000, self.timer)
            time.sleep(1)
            self.temp -= 1
        self.root.after(1000, self.timer)
        #
        # self.time_label.config(text=f"time: {minute.get()}:{second.get()}")
        # self.time_label.after(1000, self.timer)
        # # self.root.update()






    def create_button_in_middle_frame(self):
        for i in range(BOARD_SIZE):
            tk.Grid.columnconfigure(self.middle_frame, i, weight=1)
        for j in range(BOARD_SIZE):
            tk.Grid.rowconfigure(self.middle_frame, j, weight=1)
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.make_button(self.board[i][j], i, j)

    def make_button(self, button_char, row, col, rowspan=1, columnspan=1):
        button = tk.Button(self.middle_frame, text=button_char, **CUBES_BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tk.NSEW)
        self._buttons[button_char] = button

    def run(self):
        self.main_window.mainloop()


board = randomize_board(LETTERS)
# print(board)
g = BoggleGui(board)
g.run()

# text=f"time: {self.time_var.get()}",
