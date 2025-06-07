# f = open("day4/17/17_32.txt")
# a = [int(s) for s in f]
# sum_pari = []
# for i in range(len(a)-1):
#     if (a[i] + a[i+1]) == max(a):
#         sum_pari.append(a[i]**2 + a[i+1]**2)
# print(len(sum_pari), max(sum_pari))



# f = open("day4/17/17_33.txt")
# a = [int(s) for s in f]
# sum_par = []
# for i in range(len(a)-1):
#     if (a[i] % 111 == min(a)) or (a[i+1] % 111 == min(a)):
#         sum_par.append(a[i] + a[i+1])
# print(len(sum_par),max(sum_par))



# f = open("day4/17/17_34.txt")
# a = [int(s) for s in f]
# min7 = min([x for x in a if x % 7 == 0])
# sum_par = []
# for i in range(len(a)-1):
#     if a[i] % min7 == 0 and a[i+1] % min7 == 0:
#         sum_par.append(a[i] + a[i+1])
# print(len(sum_par), max(sum_par))



# f = open("day4/17/17_35.txt")
# a = [int(s) for s in f]
# min5 = min([x for x in a if len(str(x)) == 3 and x % 10 == 5])
# sum_par = []
# for i in range(len(a)-1):
#     if (len(str(a[i])) == 3 or len(str(a[i+1])) == 3) and (a[i] + a[i+1]) % min5 == 0:
#         sum_par.append(a[i] + a[i+1])
# print(len(sum_par), max(sum_par))



# f = open("day4/17/17_36.txt")
# a = [int(s) for s in f]
# min41 = min([x for x in a if x > 0 and x % 41 == 0])
# sum_par = []
# for i in range(len(a)-1):
#     if a[i] != a[i+1] and abs(a[i]- a[i+1]) % min41 == 0:
#         sum_par.append(a[i] + a[i + 1])
# print(len(sum_par), max(sum_par))



# f = open("day4/17/17_37.txt")
# a = [int(s) for s in f]
# cnt32 = len([x for x in a if x % 32 == 0])
# sum_par = []

# for i in range(len(a)-1):
#     if (a[i]< 0 or a[i+1] < 0) and (a[i] + a[i+1]) < cnt32:
#         sum_par.append(a[i] + a[i+1])
# print(len(sum_par), max(sum_par))


# f = open("day4/17/17_38.txt")
# a = [int(s) for s in f]
# min15 = min([x for x in a if len(str(abs(x))) == 3 and abs(x) % 100 == 15])
# sum_3 = []
# for i in range(len(a)- 2 ):
#     if ((a[i] >= 0 and a[i+1] >= 0 and a[i+2] >= 0 ) or (a[i] <= 0 and a[i+1] <= 0 and a[i+2] <= 0 )) and min(a[i: i+3]) * max(a[i: i+3]) > min15 ** 2 :
#         sum_3.append(min(a[i: i+3]) * max(a[i: i+3]))
# print(len(sum_3), min(sum_3))



# f = open("day4/17/17_39.txt")
# a = [int(s) for s in f]
# min6 = min([x for x in a if x > 0 and len(str(x)) == 4 and x % 10 ==6  ])
# sum3 = []
# for i in range(len(a) - 2):
#     if (len(str(abs(a[i]))) == 4) + (len(str(abs(a[i+1]))) == 4) + (len(str(abs(a[i+2]))) == 4) == 1 and sum(a[i:i + 3]) <= min6:
#         sum3.append(sum(a[i:i+3]))
# print(len(sum3), max(sum3))


# f = open("day4/17/17_40.txt")
# a = [int(s) for s in f]
# max43 = max([x for x in a if (len(str(abs(x)))) == 5 and abs(x) % 100 == 43])
# sum_3 = []
# for i in range(len(a)-2):
#     check = [x for x in a[i:i+3] if (len(str(abs(x)))) == 5 and abs(x) % 100 == 43]
#     if len(check) >= 1 and (a[i] ** 2 + a[i+1] ** 2 + a[i+3] ** 2) <= max43 **2 :
#         sum_3.append(a[i]**2 + a[i+1]**2+ a[i+2]**2)
# print(len(sum_3), min(sum_3))



f = open("day4/17/17_40.txt")
a = [int(s) for s in f]
sum_otr = sum([x for x in a if x < 0 ])
sum3 = []
for i in range(len(a)-2):
    if max(a[i:i+3]) * min(a[i:i+3]) > sum_otr:
        sum3.append(sum(a[i:i + 3 ]))
print(len(sum3), abs(max(sum3)))