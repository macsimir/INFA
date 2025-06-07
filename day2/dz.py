# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return F(n-1) * (n+1) + 5
# print(F(7)) 



# def F(n):
#     if n == 1:
#         return 1 
#     if n > 1 and n % 2 != 0:
#         return n + 5*F(n-2)
#     if n > 1 and n % 2 == 0:
#         return 2 * n * F(n-1)
    
# print(F(9))


# F = [0]*3000
# for n in range(1,3000):
#     if n == 1:
#         F[n]=1
#     if n > 1:
#         F[n] = 2 *n * F[n-1]-1
# print(F[2000]/F[1997])  

# def F(n):

#     if n >= 2025:

#         return n

#     return n // 2 + F(n + 3)

# print(F(2020) - F(2023))


# def F(n):
#     if n >= 2023:
#         return n 
#     return n // 3 + F(n + 2)
# print(F(2015)- F(2018))



# F = [0]*3000
# for n in range(1,3000):
#     if n == 1:
#         F[n]=1
#     if n > 1:
#         F[n] = n * F[n-1]
# print((F[2024]//15 - F[2023]) // F[2021])


# def F(n):
#     if n == 1:
#         return 2
#     if n == 2:
#         return 3
#     if n > 2 and n % 2 != 0:
#         return (F(n-2)+F(n-2))/7
#     if n > 2 and n % 2 == 0:
#         return 7 * n - (F(n-1)/ 2 + 5)
# print(F(40))



# F = [0] * 10_000
# for n in range(0,10000):
#     if n < 2:
#         F[n] = n
#     if n >= 2 and n % 2 == 0:
#         F[n] = F[n/2]+1
#     if n >= 2 and n % 2 != 0:
#         F[n] = F[3 * n + 1] + 1
# print(F[1:10_000])




# from functools import lru_cache
# @lru_cache(maxsize=None) 
# def F(n):
#     if n < 2:
#         return n
#     if n % 2 == 0:
#         return F(n // 2) + 1
#     else:
#         return F(3 * n + 1) + 1

# count = 0
# for n in range(1, 10001):
#     if F(n) > 200:
#         count += 1
# print(count)


# def task(start,end):
#     if start > end:
#         return 0
#     if start == end :
#         return 1
#     if start < end:
#         return task(start+1, end) + task(start*2, end) + task(start**2 , end)
# print(task(2,28))



# def task(start,end):
#     if start == 5:
#         return 0
#     if start > end:
#         return 0
#     if start == end :
#         return 1
#     if start < end:
#         return task(start +1,end) + task(start*3,end)
    
# print(task(1,21))



# def task(start,end):
#     if start == 14:
#         return 1
#     if start == 26:
#         return 0
#     if start > end: 
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task(start + 2, end) + task(start*2, end)
# print(task(2,56))



# def task(start,end):
#     if start == end:
#         return 1 
#     if start < end:
#         return 0
#     if start > end:
#         return task(start-1,end)+task(start-3,end)+task(start//2, end)
    
# print(hex(task(22,2)))



# s = 16 ** 3250 + 8 ** 2850 - 4 **100 -2 
# print(bin(s)[2:].count("1"))


# s = 256 ** 360 + 128 ** 89 - 32 ** 53
# print(bin(s)[2:].count("0"))


# s = 64**128 - 16**64 +16**16 -4**4
# cnt = 0
# while s > 0:
#     if s % 4 == 0:
#         cnt += 1 
#     s = s // 4
# print(cnt)



# s = 1296**53 + 216**16 + 36**101 -6 
# cnt = 0 
# while s > 0:
#     if s % 6 == 5:
#         cnt += 1 
#     s = s // 6 
# print(cnt)




# from string import ascii_uppercase 
# print(ascii_uppercase)
# for x in "0123456789ABCDEF":
#     s = int(f"DB24{x}FCD16", 16)+ (f"7FC{x}A8")
#     if s % 3 == 0:
#         print(x, s // 3)

# from string import ascii_uppercase 
# print(ascii_uppercase)
# for x in "0123456789ABCDEF":
#     s = int(f"DB24{x}FCD16" + f"7FC{x}A8", 16)  # Added base=16
#     if s % 3 == 0:
#         print(x, s // 3)


# "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for x in "0123456789ABCDEFGH":
#     s = int(f'AB5{x}3', 18) + int(f'EF{x}13', 18)
#     if s % 17 == 0:
#         print(x,s // 17)



###Операнды арифметического выражения записаны в системе счисления с основанием 23.
# 13yx923 + 22y2223
# В записи чисел переменными x и y обозначены неизвестные цифры из алфавита 23-ричной системы счисления. Определите наибольшее значение x, при котором значение данного арифметического выражения кратно 2 при любом значении y. Для найденного значения x вычислите целую часть частного от деления значения арифметического выражения на 18 при y = 6 и укажите его в ответе в десятичной системе счисления. Основание системы счисления в ответе указывать не нужно.
# "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
from string import ascii_uppercase 

y = 6
for x in "0123456789ABCDEFGHIJKLM":
    s = int(f'13{y}{x}9' + f'22{y}22',23)
    if s % 2 != 0:
        pass
        # print(x, s // 18)
    else:
        print(x, s // 18)
