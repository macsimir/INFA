# s = 4096 ** 210 - 1024 **67 + 256 **32 - 64
# print(bin(s)[2:].count("1"))


# s = 16384 ** 25 + 16777216 ** 14 - 4194304
# print(bin(s)[2:].count("0"))


# s = 65536 ** 5 * 1024 ** 33 + 1048576 ** 12 - 16
# digts = []
# while s > 0:
#     digts.append(s%4)
#     s =s // 4
# print(digts.count(3))


# s = 9 **8 + 3**24 - 3*7
# cnt2 = 0
# while s > 0:
#     if s  % 3 == 2:
#         cnt2 += 1 
#     s = s // 3
# print(cnt2)


# for x in "0123456789ABCD":
#     s = int(f"AB31{x}", 14) + int(f"213{x}CA", 14)
#     if s % 13 == 0:
#         print(x, s // 13)


# from string import ascii_uppercase
# print(ascii_uppercase)
# for x in "0123456789ABCDEFGHIJ":
#     s = int(f"D49{x}1" , 20) + int(f'48A3{x}', 20)
#     if s % 13 == 0:
#         print(x,s//13)


# for x in range(1,2031):
#     s = 3 ** 100 - x
#     cnt0 = 0
#     while s > 0:
#         if s % 3 == 0:
#             cnt0 += 1 
#         s = s // 3
#     if cnt0 == 5:
#         print(x)


# for x in range(1,2031):
#     s = 7 ** 91 + 7 ** 160
#     cnt0 = 0 
#     while s > 0:
#         if s % 7 == 0:
#             cnt0 += 1 
#         s //=7
#         if cnt0 == 70:
#             print(x)


# def to_4(x):
#     s = ""
#     while x > 0:
#         s += str(x % 4)
#         x = x //4 
#     return s[::-1]

# a = []
# for x in range(1,3001):
#     s = 4 ** 210 + 4 ** 110 - x
#     a.append([to_4(s).count("0"),-x])
# print(max(a))