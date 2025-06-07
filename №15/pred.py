# def DEL(n,m):
#     """натуральное число n елится без остатка на натуральное число m"""
#     return n % m == 0


# #Решение через флаги
# for A in range(1,1000):#Перебираем все натуральные числа для формулы
#     A_p = True #Подходит ли вакцина нам
#     for x in range(1,1000):
#         if ((DEL(x,A) and DEL(x,20)) <= ((not(DEL(x,20))) or DEL(x,25))) == False: #Нужно найти вакнцину , от котой людям становиться плохо
#             A_p = False #Вакцина не подходит
#             break #Прерываем если вакцина плохая 
#     if A_p: #Если с вакциной все было хорошо
#         print(A)




# def DEL(n,m):
#     return n % m == 0

# for A in range(1,1000):
#     A_p = True
#     for x in range(1,1000):
#         if (DEL(A,24) and ((DEL(x,72) and DEL(x,24)) <= DEL(x,A))) == 0:
#             A_p = False
#             break
#     if A_p:
#         print(A)



# def DEL(n,m):
#     return n % m == 0

# for A in range(1,10000):
#     for x in range(1,10000):
#         if (DEL(A,4) and ((not(DEL(2025, A))) <= (DEL(x,1111)<= DEL(2024,A)))) == False:
#             break 
#     else:
#         print(A)



# for A in range(1,10000):
#     for x in range(1,10000):
#         if (((x & 14 !=0) or (x & 17 != 0)) <= ((x &18 == 0) <= (x & A != 0))) == 0:
#             break
#     else:
#         print(A)
#         break



# for A in range(1,10000):
#     for x in range(1,10000):
#         if ((x % 18 == 0) or (x & 12 != 0) or (x & 45 != 0 )<= (x & A == 0)) == 0:
#             break
#     else:
#         print(A)


# for A in range(1,1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if ((15*x + y > A) or (x >= 40) or ( y >= 80)) == 0:
#                 break #ОТоситься только к y

#         if ((15 * x + y > A) or (x >= 40) or (y >= 80)) == 0:
#             break #Выкидывает из x
#     else:
#         print(A)



# P = list(range(3,18+1))
# Q = list(range(11,24+1))
# A = []
# for x in range(1,100):
#     if (((x in P) and (x in Q)) <= (x in A)) == False:
#         # print((((x in P) and (x in Q)) <= (x in A)))
#         A.append(x)
#         # print((((x in P) and (x in Q)) <= (x in A)))
# print(A)
# # Нам нужно найти длину из за этого вычитаем 18 -11 




# P = list(range(16,59+1))
# Q = list(range(27,71+1))
# A = []
# for x in range(1,100):
#     if ((not(x in A)) <= ((x in P) <= (not(x in Q)))) == 0:
#         A.append(x)
# print(A)
# # 27-59 = 32 Ответ



P = list(range(11,28+1))
Q = list(range(21,42+1))
A = list(range(1,100))
for x in range(1,100):
    if (((x in P) <= (x in Q)) <= (not(x in A))) == 0:
        A.remove(x)
print(A)
# 11 - 20
