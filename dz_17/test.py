# f = open('dz_17/1.txt')
# a = [int(s) for s in f]
# max3 = max([q for q in a if q % 3 == 0])
# sum_par = []
# cnt = 0

# for i in range(len(a)-1):
#     if (a[i]+ a[i+1]) == max3:
#         cnt += 1
#         sum_par.append((a[i]+a[i+1]) ** 2)
# print(cnt, max(sum_par),sep="")


# f = open("dz_17/2.txt")
# a = [int(s) for s in f]
# sum_par = []
# cnt = 0
# for i in range(len(a)-1):
#     if (a[i] % 176 == min(a)) + (a[i+1] % 176 == min(a)) >= 1:
#         cnt += 1 
#         sum_par.append(a[i]+a[i+1])
# print(cnt,min(sum_par))
cnt = 0
sum_par = []
f = open("dz_17/3.txt")
a = [int(s) for s in f]
for i in range(len(a)-1):
    if str(a[i])[-1:] == str(a[i+1])[-1:] and int(str(a[i])[-1:])% 2 == 0 and int(str(a[i+1])[-1:]) % 2 == 0:
        sum_par.append(abs(a[i]) * abs(a[i+1]))
        cnt += 1 
print(cnt,max(sum_par))