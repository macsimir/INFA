# """1"""
# s = "1" + "8" * 80
# while "18" in s or "288" in s or "3888" in s: #Нахождение 18 или 288 или 3888
#     if "18" in s:
#         s = s.replace("18","2",1) #Первая слева замена
#     else:
#         if "288" in s:
#             s = s.replace("288","2",1) #Замена 288 на 3 
#         else:
#             s = s.replace("3888","2",1)
# print(s)


"""2"""
# s = ">"+"1" * 10 + "2" * 20 + "3" * 30 
# while ">1" in s or ">2" in s or ">3" in s: #Нахождение 18 или 288 или 3888
#     if ">1" in s:
#         s = s.replace(">1","22>",1) #Первая слева замена
#     if ">2" in s:
#         s = s.replace(">2","2>",1) #Замена 288 на 3 
#     if ">3" in s:
#         s = s.replace(">3","1>",1)
# print(s.count("2") * 2 + s.count("1") * 1 + s.count("3")*3)
# print(sum(map(int , s[:-1])))


"""3"""
# for n in range(4,1000):
#     s = "5" + "2" * n
#     while "52" in s or "2222" in s or "1222" in s: #Нахождение 18 или 288 или 3888
#         if "52" in s:
#             s = s.replace("52","11",1) #Первая слева замена
#         if "2222" in s:
#             s = s.replace("2222","5",1) #Замена 288 на 3 
#         if "1122" in s:
#             s = s.replace("1122","25",1)
#     # print(sum(map(int,s)),n)
#     if sum(map(int,s)) == 72:
#         print(n)


"""4"""
# for n in range(4,10000):
#     s = "4" + "1" * n
#     while "31" in s or "411" in s or "1111" in s:
#         if "31" in s:
#             s = s.replace("31","1",1) 
#         if "411" in s:
#             s = s.replace("411","13",1) 
#         if "1111" in s:
#             s = s.replace("1111","4",1)
#     if sum(map(int,s)) == 40:
#         print(n)
#         break


"""5"""
# def is_prime(x):
#     """Проверка на простое число """
#     for i in range(2,x): #Число простое если оно делится на себя и на 1 
#         if x % i == 0:
#             return False
#     else:
#         return True

# for n in range(1,1000):
#     s = ">"+"0" * 37 + "1" * n + "2" *46
#     while ">1" in s or ">2" in s or ">0" in s:
#         if ">1" in s:
#             s = s.replace(">1","22>",1) 
#         if ">2" in s:
#             s = s.replace(">2","2>",1) 
#         if ">0" in s:
#             s = s.replace(">0","1>",1)
#     if is_prime(sum(map(int,s[:-1]))):
#         print(n)


"""6"""
# a = []
# for n in range(3,10000):
#     s = "1" + "2" * n 
#     while "12" in s or "322" in s or "222" in s:
#         if "12" in s:
#             s = s.replace("12","2",1) 
#         if "322" in s:
#             s = s.replace("322","21",1) 
#         if ">0" in s:
#             s = s.replace("222","3",1)
#     a.append(s.count("3") * 3 + s.count("2") *  2 + s.count("1"))
# print(max(a))




# max_v = 0
# for n in range(4,10000): #(3 < n < 10 000).
#     s = "7" + n * "2"
#     while "72" in s or "322" in s or "2222" in s:
#         if "72" in s:
#             s.replace("72", "2",1)
#         if "322"in s:
#             s.replace("322","27",1)
#         if "222" in s:
#             s.replace("222","3",1)
#     max_v = max(max_v,sum(list(map(int , s))))
# print(max_v)