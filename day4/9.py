# cnt = 0
# f = open("day4/9/9_1.txt")
# for s in f:
#     a = list(map(int, s.split()))
#     if 3 * abs(a[0]- a [1]) == a[2] or 3 * abs(a[0]- a [2]) == a[1] \
#     or 3 * abs(a[1]- a [2]) == a[0]: #Модуль abs
#         cnt += 1 
# print(cnt)



# f = open("day4/9/9_2.txt")
# cnt = 0
# for s in f:
#     a = list(map(int , s.split()))
#     povt = [x for x in a if a.count(x)> 1]
#     nepovt = [x for x in a if a.count(x) == 1]
#     if len(povt) == 3 and sum(povt) ** 2 > sum(nepovt)**2:
#         cnt += 1
# print(cnt)




# f = open("day4/9/9_3.txt")
# cnt = 0
# for s in f:
#     a = list(map(int , s.split()))
#     povt = [x for x in a if a.count(x)> 1]
#     nepovt = [x for x in a if a.count(x) == 1]
#     if len(povt) > 0 and sum(nepovt) % 2 != 0:
#         cnt += 1
# print(cnt)




# f = open("day4/9/9_4.txt")
# cnt = 0
# for s in f:
#     a = list(map(int , s.split()))
#     chet = [x for x in a if x % 2 == 0]
#     nechet = [x for x in a if x % 2 != 0]
#     if len(set(a)) == 5 and len(nechet) > len(chet) and sum(nechet) > sum(chet):
#         cnt += 1
# print(cnt)




# f = open("day4/9/9_5.txt")
# cnt = 0
# for s in f:
#     a = list(map(int , s.split()))
#     povt = [x for x in a if a.count(x)> 1]
#     nepovt = [x for x in a if a.count(x) == 1]
#     if len(set(a)) == 5 and sum(povt) < sum(nepovt):
#         cnt += 1    
# print(cnt)





# f = open("day4/9/9_6.txt")
# cnt = 0
# for s in f:
#     a = list(map(int , s.split()))
#     povt = [x for x in a if a.count(x)> 1]
#     nepovt = [x for x in a if a.count(x) == 1]
#     if len(povt) > 0 and (sum(povt) / len(povt)) > (sum(nepovt) / len(nepovt)):
#         cnt += 1 
# print(cnt)




# f = open("day4/9/9_7.txt")
# cnt = 0
# for s in f:
#     a = list(map(int , s.split()))
#     povt = [x for x in a if a.count(x)> 1]
#     nepovt = [x for x in a if a.count(x) == 1]
#     if len(povt) == 4 and len(set(povt)) == 2 and (sum(nepovt) / len(nepovt) < sum(povt)):
#         cnt += 1 
# print(cnt)



# num = 1
# f = open("day4/9/9_8.txt")
# for s in f:
#     a = list(map(int , s.split()))
#     povt_nech = [x for x in a if a.count(x) > 1 and sum(map(int , str(x)) ) % 2 != 0]
#     if sorted(a) == a and len(povt_nech) > 0:
#         print(num)
#     num += 1 



# cnt = 0 
# f = open("day4/9/9_9.txt")
# for s in f:
#     a = list(map(int , s.split()))
#     povt = [x for x in a if a.count(x)> 1]
#     nepovt = [x for x in a if a.count(x) ==  1]
#     if len(povt) > 0  and len(nepovt) > 0 and sum(nepovt) / len(nepovt) < sum(povt) / len(povt):
#         cnt = cnt +1 
# print(cnt)



