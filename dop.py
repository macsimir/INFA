# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (x <= y) and z and (not(w)) == 1: #F = 1
#                     print(x,y,z,w)



"""5"""
# for n in range(1,1000):
#     n2 = bin(n)[2:]
#     if n % 3 == 0:
#         n2 +=  n2[-3:]
#     else:
#         n2 += bin((n % 3) * 2)[2:]
#     r = int(n2,2)
#     if r < 130:
#         print(n)



"""7"""
# V1 = 1920 * 1080 * 23
# V2 = 1280 * 1024 * 21
# print(((V1-V2)*120)/ 2 **13)

"""8"""
# from itertools import product
# numb1 = 0
# for word in product(sorted("ТЕОРИЯ"), repeat=6):
#     if (numb1 % 2 != 0) and word[0] not in "Р" and word[0] not in "Т" and word[0] not in "Я" and word.count("И") >= 2:
#         print(numb1)
#     numb1 += 1


"""9"""
# f = open("9")
# numb = 1
# for s in f:
#     a = list(map(int , s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     nepovt = [x for x in a if a.count(x) == 1]
#     if len(povt) == 3 and povt[0] > (sum(nepovt)/len(nepovt)):
#         print(numb)
#     numb += 1


# from math import log2,ceil
# for len_s in range(1,1000): #len_s серийный номер
#     A = 10 + 52 + 963 #МОЩНОСТЬ АЛФАВИТА
#     i = (ceil(log2(A)))
#     V1 = ceil((len_s * i) / 8)
#     V2000 = V1 * 2000
#     if V2000 <= 693 * 2**10:
#         print(len_s)



# from math import log2 , ceil
# for A in range(1,1000):
#     i = ceil(log2(A))
#     V1 = ceil((172 * i) / 8) #Длинну умножаем на i и делим на 8, чтобы получить целое число байт
#     if V1*365_984 >= 54 * 2 **20:
#         print(A)
#         break
# for n in range(4,1000):
#     s = "7" + n * "8"
#     while "78" in s or "678" in s or "8888" in s:
#         if "688" in s:
#             s.replace("688", "87",1)
#         if "8888" in s:
#             s.replace("8888", "6",1)
#         if sum(map(int, s )) == 61:
#             print(n)
#             break


# from ipaddress import ip_network

# ip_net = ip_network("45.172.106.203/255.255.252.0",0)
# for i in ip_net:
#     print(i)

def to_9(n):
    rec = ""
    while n > 0:
        rec += str(n % 9)
        n //= 9
    return rec[::1]
    
for x in range(1,3000):
    s = 9 **150 + 9 ** 30 - x
    if to_9(s).count("0")== 122:
        print(x)
        break