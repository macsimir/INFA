# a = []
# for n in range(1,1000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 = "1" + n2 + "0"
#     else:
#         n2 = "11" + n2 + "11"
#     r = int(n2,2)
#     if r > 52 :
#         a.append(r)

# print(min(a))




# for n in range(1,1000):
#     n2 = bin(n)[2:]
#     if n2.count("1") % 2 == 0:
#         n2 += "0"
#         n2 = "10" + n2[2:]
#     else:
#         n2 += "1"
#         n2 = "11" + n2[2:]
#     r = int(n2,2)
#     if r >= 16:
#         print(n)



# for n in range(1,1000):
#     n2 = bin(n)[2:]
#     if n2.count('1') % 2 == 0:
#         n2 += "0"
#         n2 = "100" + n2[3:]
#     else:
#         n2 += "1"
#         n2 = "111" + n2[3:]
#     r = int(n2,2)
#     if r > 128:
#         print(n)
#         break



# for n in range(1,13):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 = "10" + n2
#     else:
#         n2 = "1" + n2 + "01"
#     r = int(n2,2)
#     print(r)



# a = []
# for n in range(1,1000):
#     n2 = bin(n)[2:]
#     if n % 3 == 0:
#         n2 += n2[-3:]
#     else:
#         n2 += bin((n % 3 ) * 3)[2:]
#     r = int(n2,2)
#     if r <= 170: 
#         a.append(r)
# print(max(a))



# def to_3(x):
#     """Перевод в троичную систему """
#     s = ""
#     while x > 0:
#         s += str(x % 3) + s
#         x = x // 3
#     return s
# a = []
# for n in range(1,100):
#     n3 =  to_3(n)
#     if n % 3 == 0:
#         n3 += n3[-2:]
#     else:
#         n3 += to_3((n % 3) * 5 )
#     r = int(n3,3)
#     if r > 178:
#         a.append(r)
# print(min(a))



def to_5(x):
    s = ""
    while x > 0:
        s += str(x % 5)
        x = x // 5
    return s[::-1]
for n in range(1,1000):
    n5 = to_5(n)
    if n % 10 == 0:
        n5 += n5[-2:]
    else:
        n5 = to_5((n % 10 ) * 3) + n5
    r = int(n5,5)
    if r < 281:
        print(n)