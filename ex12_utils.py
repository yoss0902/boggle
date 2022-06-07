from boggle_board_randomizer import *
from copy import deepcopy


def is_valid_path(board, path, words):
    """ a function that checks if the path given
    matching a word in the words list and that the
     path is valid"""
    flag, word = _legal_move(path, board)
    if not flag:
        return
    if word not in words:
        return
    return word


def _legal_move(path, board):
    """ an helper function that makes the necessary checkups
    to determine if a path is valid"""
    used_tups = [path[0]]
    word = str(board[path[0][0]][path[0][1]])
    for i in range(1, len(path)):
        if path[i] in used_tups or (abs(path[i][0] - path[i - 1][0]) not in (0, 1)) or (
                abs(path[i][1] - path[i - 1][1]) not in (0, 1)):
            return False, word
        used_tups.append(path[i])
        row, col = path[i]
        word += board[row][col]
    return True, word


def _find_length_n(n, board, words, word, path_lst, path, row, col, flag):
    """an helper function that makes the backtracking
    in order to receive all possible path for a given
     path length or a word length"""
    word.append(board[row][col])
    if flag:
        if len(board[row][col]) > 1:
            n -= 1
    path.append((row, col))
    if n == 0:  # base case
        if "".join(word) in words:
            path_lst.append(deepcopy(path))
        path.pop()
        word.pop()
        return
    _every_possible_direction(board, col, n, path, path_lst, row, word, words, flag)
    # recursive call
    path.pop()
    word.pop()
    return


def _every_possible_direction(board, col, n, path, path_lst, row, word, words, flag):
    """ a function that covers all possible moves from a single board cell
    and contain recursive calls for every direction"""
    if col < len(board[0]) - 1 and (row, col + 1) not in path:
        _find_length_n(n - 1, board, words, word, path_lst, path, row, col + 1, flag)  # right
    if row < len(board) - 1 and (row + 1, col) not in path:
        _find_length_n(n - 1, board, words, word, path_lst, path, row + 1, col, flag)  # up
    if 0 < col and (row, col - 1) not in path:
        _find_length_n(n - 1, board, words, word, path_lst, path, row, col - 1, flag)  # left
    if 0 < row and (row - 1, col) not in path:
        _find_length_n(n - 1, board, words, word, path_lst, path, row - 1, col, flag)  # down
    if col < len(board[0]) - 1 and row < len(board) - 1 and (row + 1, col + 1) not in path:
        _find_length_n(n - 1, board, words, word, path_lst, path, row + 1, col + 1, flag)  # down right
    if col > 0 and row < len(board) - 1 and (row + 1, col - 1) not in path:
        _find_length_n(n - 1, board, words, word, path_lst, path, row + 1, col - 1, flag)  # down left
    if col < len(board[0]) - 1 and 0 < row and (row - 1, col + 1) not in path:
        _find_length_n(n - 1, board, words, word, path_lst, path, row - 1, col + 1, flag)  # up right
    if col < 0 and row < 0 and (row - 1, col - 1) not in path:
        _find_length_n(n - 1, board, words, word, path_lst, path, row - 1, col - 1, flag)  # up left


def _board_iterator(n, board, words, flag):
    """ a function that apply the backtracking on
    every cell of the board"""
    path_lst = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            _find_length_n(n - 1, board, words, [], path_lst, [], i, j, flag)
    return path_lst


def find_length_n_paths(n, board, words):
    """ a function that return a list of the
    path which are in a length of n"""
    return _board_iterator(n, board, words, False)


def find_length_n_words(n, board, words):
    """ a function that return a list of the word path
    which are in a length of the length of the word"""
    return _board_iterator(n, board, words, True)


# def max_score_paths(board, words):
#     longest_word = max(words, key=lambda word: len(word))
#     path_list = []
#     for i in range(1, len(longest_word)):
#         path_list + list(set(find_length_n_word(i, board, words)))
#     return path_list
#

def max_score_paths(board, words):
    flag = False
    path_lst = []
    for word in words:
        word_lst = []
        first_letter = word[0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if first_letter == board[i][j]:
                    _find_length_n(len(word), board, word, [], word_lst, [], i, j, False)
                    if word_lst:
                        path_lst.append(word_lst[0])
                        word_lst = []
                        flag = True
                        break
                    else:
                        _find_length_n(len(word), board, word, [], word_lst, [], i, j, True)
                        if word_lst:
                            path_lst.append(word_lst[0])
                            word_lst = []
                            flag = True
                            break
            if flag:
                break
    return path_lst





def load_words_dict(filename):
    return [word.strip() for word in open(filename, 'r') if len(word.strip()) == 3]

board = [['N', 'I', 'D', 'I'],
         ['O', 'T', 'T', 'G'],
         ['Q', 'S', 'E', 'Z'],
         ['U', 'QU', 'C', 'T']]
words = [ 'ESQU', 'ZTC']
# # print(max_score_paths(b, words))
# print(find_length_n_paths(3, board, ['ITS', 'GZC', 'TSC', 'ESQU', 'ZTC']))
# print(find_length_n_words(3, board, words))
#'ITS', 'GZC', 'TSC',
print(max_score_paths(board, words))
# v = [[(0, 1), (1, 1), (2, 1)], [(0, 1), (1, 2), (2, 1)], [(0, 3), (1, 2), (2, 1)], [(1, 1), (2, 1), (3, 2)], [(1, 2), (2, 1), (3, 2)], [(1, 3), (2, 3), (3, 2)], [(2, 2), (2, 1), (3, 1)], [(2, 3), (3, 3), (3, 2)]]
# print(v == find_length_n_path(3, board, ['ITS', 'GZC', 'TSC', 'ESQU', 'ZTC']))
