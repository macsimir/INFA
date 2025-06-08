# #27_1 A
# from math import *
# f = open("№27/27_1/27A.txt")
# points = [list(map(float, s.replace(",", ".").split()))for s in f]
# clusters = [[],[]]
# for x ,y in points:
#     if y> 0:
#         clusters[0].append([x,y])
#     else:
#         clusters[1].append([x,y])
# best_centr = [[],[]]
# for i in range(2):
#     min_sum_dist = 10**8
#     for x1,y1 in clusters[i]:
#         sum_10 = 0 #Растояние
#         for x2,y2 in clusters[i]:
#             sum_10 += dist([x1,y1],[x2,y2])
#         if sum_10 < min_sum_dist:
#             min_sum_dist = sum_10
#             best_centr[i] = [x1,y1]
# P_x = sum([x for x , y in best_centr]) / 2
# P_y = sum([y for x , y in best_centr]) / 2
# print(P_x * 10_000, P_y * 10_000)




#27_1 B
# from math import *
# f = open("№27/27_1/27B.txt")
# points = [list(map(float, s.replace(",", ".").split()))for s in f]
# clusters = [[],[],[]]
# for x ,y in points:
#     if y < 0:
#         clusters[0].append([x,y])
#     elif x > 2:
#         clusters[1].append([x,y])
#     else:
#         clusters[2].append([x,y])
# best_centr = [[],[],[]]
# for i in range(3):
#     min_sum_dist = 10**8
#     for x1,y1 in clusters[i]:
#         sum_10 = 0 #Растояние
#         for x2,y2 in clusters[i]:
#             sum_10 += dist([x1,y1],[x2,y2])
#         if sum_10 < min_sum_dist:
#             min_sum_dist = sum_10
#             best_centr[i] = [x1,y1]
# P_x = sum([x for x , y in best_centr]) / 3
# P_y = sum([y for x , y in best_centr]) / 3
# print(P_x * 10_000, P_y * 10_000)




#27_1 A
# f = open("№27/27_2/27A.txt")
# point = [map(float,s.replace(",", '.').split())for s in f]
# k = 2 #Количество кластеров 
# clusters = [[],[]] #Два кластера
# for x , y in point:
#     """Перебираем все точки для кластера"""
#     if y > 0:
#         clusters[0].append([x,y])
#     else:
#         clusters[1].append([x,y])
# best_centr = [[],[]]
# for i in range(k):
#     """Перебираем все цинтроиды"""
#     min_sum_dist = 10*10
#     for x1,y1 in clusters[i]:
#         for x2,y2 in clusters[i]:
#             sum_dist = 0#Растояние между точками
#             sum_dist += abs(x2-x1) + abs(y2-y1)
#         if sum_dist < min_sum_dist:
#             min_sum_dist = sum_dist
#             best_centr[i] = [x1,y1]

# P_x = sum([x for x,y in best_centr]) / k
# P_y = sum([y for x,y in best_centr]) / k
# print(P_x * 10_000, P_y * 10_000)



#27_1 B
# f = open("№27/27_2/27B.txt")
# point = [map(float,s.replace(",", '.').split())for s in f]
# k = 3 #Количество кластеров 
# clusters = [[],[],[]] #Два кластера
# for x , y in point:
#     """Перебираем все точки для кластера"""
#     if y > 0:
#         clusters[0].append([x,y])
#     else:
#         clusters[1].append([x,y])
# best_centr = [[],[],[]]
# for i in range(k):
#     """Перебираем все цинтроиды"""
#     min_sum_dist = 10*10
#     for x1,y1 in clusters[i]:
#         for x2,y2 in clusters[i]:
#             sum_dist = 0#Растояние между точками
#             sum_dist += abs(x2-x1) + abs(y2-y1)
#         if sum_dist < min_sum_dist:
#             min_sum_dist = sum_dist
#             best_centr[i] = [x1,y1]

# P_x = sum([x for x,y in best_centr]) / k
# P_y = sum([y for x,y in best_centr]) / k
# print(abs(P_x * 10_000), abs(P_y * 10_000))


#Целая часть и модуль
# print(56//10) # 5 
# print(int(56// 10)) #5
# print(-56// 10) # -6
# print(int(-56// 10)) # - 6
# -5.6 -> -6





#
# from math import dist
# f = open("№27/27_3/27A.txt")
# points = [map(float, s.replace(",",".").split()) for s in f]
# k = 2
# cluster = [[],[]]
# for x,y in points:
#     if y > 0:
#         cluster[0].append([x,y])
#     else:
#         cluster[1].append([x,y])
# anti_centr = [[],[]]
# for i in range(k):
#     max_sum_dist = 0 
#     for x1,y1 in cluster[i]:
#         sum_dist =0
#         for x2,y2 in cluster[i]:
#             sum_dist += dist([x1,y1], [x2,y2])
#         if sum_dist > max_sum_dist:
#             max_sum_dist = sum_dist
#             anti_centr[i] = [x1,y1]
# print(anti_centr)

# from math import dist
# f = open("№27/27_3/27B.txt")
# points = [map(float, s.replace(",",".").split()) for s in f]
# k = 3
# cluster = [[],[],[]]
# for x,y in points:
#     if y > 5:
#         cluster[0].append([x,y])
#     if y > -5:
#         cluster[1].append([x,y])

#     else:
#         cluster[2].append([x,y])
# anti_centr = [[],[],[]]
# for i in range(k):
#     max_sum_dist = 0 
#     for x1,y1 in cluster[i]:
#         sum_dist =0
#         for x2,y2 in cluster[i]:
#             sum_dist += dist([x1,y1], [x2,y2])
#         if sum_dist > max_sum_dist:
#             max_sum_dist = sum_dist
#             anti_centr[i] = [x1,y1]
# print(anti_centr)
# print(len(cluster[0]), len(cluster[1]), len(cluster[2]))

