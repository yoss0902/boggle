import tkinter as tk
from boggle_board_randomizer import *
import time
from tkinter import messagebox
from copy import deepcopy

BUTTON_HOVER_COLOR = "gray"
REGULAR_COLOR = "lightgray"
BUTTON_ACTIVE_COLLOR = "slateblue"
CUBES_BUTTON_STYLE = {"font": ("Courier", 30),
                      "borderwidth": 1,
                      "relief": tk.RAISED,
                      "bg": REGULAR_COLOR,
                      "activebackground": BUTTON_ACTIVE_COLLOR,
                      "height":3, "width":6}

board = [['N', 'I', 'D', 'I'],
         ['O', 'T', 'TC', 'G'],
         ['Q', 'S', 'E', 'Z'],
         ['U', 'QU', 'C', 'T']]






class Boggle:

    def __init__(self, words):
        self.root = tk.Tk()
        self.root.title("Boggle Game")
        self.outer_frame = tk.Frame(self.root, width=400, height=400, bg=REGULAR_COLOR,
                                    highlightbackground=REGULAR_COLOR,
                                    highlightthickness=5)
        self.outer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.words = words


        # time
        self.time_flag = False
        self.second_count = 10
        self.minute_str = tk.StringVar()
        self.second_str = tk.StringVar()
        self.minute_str.set("03")
        self.second_str.set("00")
        self.time_label = tk.Label(self.outer_frame, font=("david", 30),
                                   text= "time : 03:00 ",
                                   bg=REGULAR_COLOR,
                                   relief="ridge", width=15)
        self.time_label.grid(row=0, column=0, rowspan=1, columnspan=1)


        # score
        self.score = 0
        self.score_to_user = tk.StringVar()
        self.score_to_user.set(self.score)


        self.score_label = tk.Label(self.outer_frame, text=f"score: ", font=("david", 30),
                                    bg=REGULAR_COLOR, width=15, relief="ridge")
        self.score_label.grid(row=1, column=0, rowspan=1, columnspan=1)

        # board
        self.board = [["*"]*BOARD_SIZE]*BOARD_SIZE
        self.buttons = {}
        self.middle_frame = tk.Frame(self.outer_frame)
        self.middle_frame.grid(row=1, column=1, rowspan=2, columnspan=1)


        #current_guess
        self.word_to_user = tk.StringVar(self.outer_frame)
        self.word = ""
        self.word_to_user.set(self.word)
        self.word_path = []
        self.current_guess_label = tk.Label(self.outer_frame, font=("david", 30), text="word: ", bg=REGULAR_COLOR,
                                             relief="ridge", height=1, width=33)
        # self.current_guess_label.bind("<Button-1>",self.updating_variables)
        self.current_guess_label.grid(row=0, column=1, rowspan=1, columnspan=1)



        #word_list
        self.word_lst = []
        self.word_list_to_user = tk.StringVar()
        self.word_list_to_user.set(self.word_lst)
        # self.word_lst_to_print = tk.StringVar(self.word_list)
        self.found_words = tk.Label(self.outer_frame, text="found words: ", font=("Ariel", 20),height=18, width=20, relief="ridge")
        self.found_words.grid(row=2, column=0, rowspan=1, columnspan=1)

        #start_butoon
        # self.start = self.start()
        self.start_button = tk.Button(self.outer_frame, text="start", bg="blue", font=("david", 15), width=15,
                                      relief="ridge", command=self.start)
        self.start_button.grid(row=0, column=2, rowspan=1, columnspan=1)


        #instruction
        self.instruction_lable = tk.Label(self.outer_frame, text="game instruction", font=("Ariel", 15),
                                          bg="yellow", relief="ridge")
        self.instruction_lable.grid(row=2, column=2, rowspan=1, columnspan=1)


        # check word button
        self.check_button = tk.Button(self.outer_frame, text = "check the word", bg = "green", font = ("david", 15),
                                      width = 15, relief = "ridge", command = self.check_complete_word)
        self.check_button.grid(row = 1, column = 2, rowspan=1, columnspan=1)

        self.create_button_in_middle_frame()
        self.time_label.after(1000, self.run_timer)

    def run(self):
        self.root.mainloop()

    def create_button_in_middle_frame(self):
        button = deepcopy(self.board)
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                button[i][j] = tk.Button(self.middle_frame, text=self.board[i][j], **CUBES_BUTTON_STYLE, command = self.updating_variables(i,j))
                button[i][j].grid(row=i, column=j, rowspan=1, columnspan=1, sticky=tk.NSEW)
                self.buttons[self.board[i][j]] = button



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
        def letter_press():
            self.word += self.board[row][col]
            self.word_to_user.set(f" word: {self.word}")
            self.current_guess_label.config(text=self.word_to_user.get())
            self.word_path.append((row, col))
        return letter_press

    def check_complete_word(self):
        if self.word in self.words and self.word not in self.word_lst:
            self.word_lst.append(self.word)
            self.word_list_to_user.set(self.word_lst)
            self.found_words.config(text=f"found words: {self.word_list_to_user.get()}")
            self.word_to_user.set("correct!")
            self.current_guess_label.config(text=f"word: {self.word_to_user.get()}")
            self.score += len(self.word_path) ** 2
            self.score_to_user.set(self.score)
            self.score_label.config(text=f" score: {self.score}")
            self.word = ""
            self.word_path = []
        else:
            self.word = ""
            self.word_to_user.set("wrong!")
            self.current_guess_label.config(text=f"word: {self.word_to_user.get()}")
            self.word_path = []

    def run_timer(self):
        if self.time_flag:
            if self.second_count > -1:
                mins, secs = divmod(self.second_count, 60)
                print(mins)
                print(secs)
                self.minute_str.set(mins)
                self.second_str.set(secs)
                self.time_label.config(text=f"time: {self.minute_str.get()}:{self.second_str.get()}")
                if self.second_count == 0:
                    self.time_flag = False
                    game_flag = messagebox.askretrycancel("popup", "game is over!")
                    print(game_flag)
                    if game_flag:
                        self.restart_game()
                    else:
                        self.exit()
                self.second_count -= 1
        self.time_label.after(1000, self.run_timer)

    def start(self):
        self.time_flag = True
        self.board = board
        self.create_button_in_middle_frame()


    def restart_game(self):
        self.second_count = 180
        self.board = randomize_board(LETTERS)
        self.create_button_in_middle_frame()
        self.time_flag = True

        self.word_lst = []
        self.word_list_to_user.set(self.word_lst)
        self.found_words.config(text=f"found words: {self.word_list_to_user.get()}")
        self.word_path = []
        self.score = 0
        self.score_to_user.set(self.score)
        self.score_label.config(text=f" score: {self.score}")
        self.word = ""
        self.word_to_user.set(self.word)
        self.current_guess_label.config(text=f"word: {self.word_to_user.get()}")
        self.minute_str.set("03")
        self.second_str.set("00")
        self.time_label.config(text=f"time: {self.minute_str.get()}:{self.second_str.get()}")


    def exit(self):
        self.root.destroy()

words = ['ESQU', 'ZTC', 'ITS', 'NID', "NOT"]
# def load_words_dict(filename):
#     return [word.strip() for word in open(filename, 'r') if len(word.strip()) == 3]
g = Boggle(words)
g.run()
