# from functools import reduce
# def count_appearances1(letter, word):
#
#     fun = lambda a, c: c + 1 if a == letter
#     # a, b = fun(0)
#
#     return reduce(fun, word ,0)
#
# def simple_generator():
#     yield "my"
#     yield "simple"
#     yield "generator"
#
# my_iter = simple_generator()
# print(next(my_iter))
# # print(next(my_iter))
# # print(next(my_iter))
# lst = [0, 9, 8, 7]
# l = iter(lst)
# print(next(l))
#
#

# class Repeater:
#     def __init__(self, it, n):
#         self.it = iter(it)
#         self.n = n
#         self.count = n
#         self.val = None
#
#     def __next__(self):
#         if self.count >= self.n:
#             self.count = 1
#             self.val = next(self.it)
#         else:
#             self.count += 1
#         return self.val
#
#     def __iter__(self):
#         return self
#
# for i in Repeater([1, 2, 3], 4):
#     # return i
#     # print(i)
#     print(i, end="")
#     #     return i
#
#
# def for_loop(iterable):
#     loop_iter = iter(iterable)
#     sential = object()
#     item = next(loop_iter, sential)
#     while item is not sential:
#         if item is not None:
#             # print(item)
#             print(item, end = "")
#         item = next(loop_iter, sential)
# #
#
# print(for_loop(Repeater([1, 2,3], 4)))
# # print(Repeater([1, 2, 3], 4))
# #
#
# def count_to_num(num):
#     if num <= 0:
#         return
#     for i in count_to_num(num - 1):
#         print("i = ", i)
#         yield i
#     yield num
#
#
# for i in count_to_num(10):
#     print(i, end="")
#
# def power_ser_iter(full_set):
#     if len(full_set) == 0:
#         yield set()
#     else:
#         item = full_set.pop()
#         for subs in power_ser_iter(full_set):
#             yield subs | {item}
#             yield subs
#
#
#
# a = power_ser_iter({1, 2})
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
#
#
# for i in power_ser_iter({1, 2, 3}) :
#     print(i, end = " ")
#
# def get_iter2(word):
#     for letter in word:
#         if letter != " ":
#             yield letter
# k = get_iter2("hello")
# print(next(k))
# print(next(k))
#
# for char in get_iter2(" h e l    l o     *"):
#     print(char, end = "")
# # print()
# print(20%3)
# print(list(range(0, 10, 3)))
# def bunch_together(iterable, n):
#     if not iterable % n:
#         iterable = iterable
#         else:
#         for i in range(n - len(iterable) % n)
#             iterable.append(None)
#
#
# tup_iter = []
# for j in range(0, len(iterable), 3):
#     tup_iter.append(j, j + 1, j + 2)
#
#
# def iter():
#     iter_ = iter(tup_iter)
#     count = 0
#     val = None
#     if count == len(tup_iter):
#         raise StopIteration
#     else:
#
#         val = next(iter_)
#         count += 1
#         return val
#
#
# return iter
# #
# z = [1,3,2]
# z.append(z)
# # z.append(z*2)
# # print(z[-1][-1][-1][-
# # print(z is z[-1])
#
# def ii(lst, n):
#     return [lst for _ in range(n)]
# lst1 = [1, 2, 3]
# s = ii(lst1, 3)
# # print(s[1] is s[2])
# x2 = [[1]*3 for _ in range(3)]
# print(id(x2[1]) == id(x2[0]))
# x3 = [[1 for _ in range(3)] for _ in range(3)]
# # print(x3[0][0] is x3[1][0])
# lst3 = ["plo", "oli", "plop"]
# print([i for i in lst3 if len(i) ==3 ])
o = lambda a: lambda b: a+b
print(o(12)(5))