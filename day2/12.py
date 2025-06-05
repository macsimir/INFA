from itertools import *
# n = 1
# for i in product("АБВГДЕЖЗИК", repeat=3):
#     word = "".join(i)
#     if word == "АЖЕ":
#         print(n)
#     n += 1 



# from itertools import *
# n = 1
# for i in product("АБВГДЕЖЗ", repeat=3):
#     word = "".join(i)
#     if n == 350:
#         print(word)
#     n += 1 



# from itertools import *
# n = 1
# for i in product(sorted("СКАНЕР"), repeat=6):
#     word = "".join(i)
#     if word.count("А") <= 3 and word.count("Н") == 2:
#         print(n)
#         break
#     n += 1 


# from itertools import *
# cnt = 0
# n = 1
# for i in product(sorted("ИНФОРМАТ"), repeat=5):
#     word = "".join(i)
#     if n % 2 != 0 and word[0] != "O" and 1<= word.count("Н") <= 2:
#         cnt += 1
#     n += 1
# print(cnt)



# cnt = 0
# for i in product("12345678", repeat=5):
#     word = "".join(i)
#     if word.count("2") == 1:
#         cnt += 1
# print(cnt)



# cnt = 0 
# for i in set(permutations("КАРЕТА", r=4)):
#     word = "".join(i)
#     if "АА" not in word:
#         cnt += 1
# print(cnt)



