# f = open("№24/24_12.txt")
# s = f.readline()

# nech = []
# buff = ""
# for sym in s: #Sym = символ
#     if len(buff) ==0 and sym in "123456789":
#         buff += sym
#     elif len(buff) > 0 and sym in "0123456789":
#         buff += sym
#     else:
#         buff = ""
#     if len(buff) > 0 and buff[-1] in "13579":
#         nech.append(buff)
# print(max(nech, key=len))


# f = open("№24/24_13.txt")
# s = f.readline()
# buff = ""
# max_buff = ""

# for sym in s:
#     if len(buff) == 0 and sym in "123456789":
#         buff += sym
#     elif len(buff) >0 and sym in "0123456789" and int(buff[-1]) + int(sym) >= 10:
#         buff += sym
#     else:
#         buff = sym
#     max_buff = max(max_buff, buff,key=len)
# print(len(max_buff))



# f = open("№24/24_14.txt")
# s = f.readline()
# buff = ""
# max_buff = ""

# for sym in s:
#     if sym in "123456789ABCDEF":
#         buff += sym
#     else:
#         buff = ""
#     max_buff = max(max_buff, buff, key=len)
# print(max_buff)
# print(len(max_buff))



# f = open("№24/24_15.txt")
# s = f.readline()
# buff = ""
# max_buff = ""
# for sym in s:
#     if len(buff) == 0 and sym in "123456789AB":
#         buff += sym
#     elif len(buff) > 0 and sym in "0123456789AB":
#         buff += sym
#     else:
#         buff = ""
#     if len(buff) > 0 and buff[-1] in "02468A":
#         max_buff = max(max_buff , buff, key=len)
# print(max_buff)
# print(len(max_buff))


# f = open("№24/24_16.txt")
# s = f.readline()
# buff , max_buff = "" , ""
# for sy in s:
#     if len(buff) == 0 and sy in "123456789ABCD":
#         buff += sy
#     elif len(buff) >= 0 and sy in "0123456789ABCD":
#         buff += sy
#     else:
#         buff = ""
#     if buff and buff[-1] in "02468AC":
#         max_buff = max(max_buff,buff,key=len)
# print(max_buff)
# print(len(max_buff))


# f = open("№24/24_17.txt")
# s = f.readline()
# buff , max_buff = "" , ""
# for sy in s:
#     if len(buff) == 0 and sy in "123456789":
#         buff += sy
#     elif len(buff) > 0 and sy in "0123456789AB":
#         buff += sy
#     else:
#         buff = ""
#     max_buff = max(max_buff, buff, key=len)
# print(len(max_buff))
# print(max_buff)


