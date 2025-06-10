from math import dist 

f = open("1/27_2/2.txt")
from math import *
points = [list(map(float, s.replace(",", ".").split()))for s in f]
clusters = [[],[],[]]
for x ,y in points:
    if y > 0:
        clusters[0].append([x,y])
    elif x > 2:
        clusters[1].append([x,y])
    else:
        clusters[2].append([x,y])
best_centr = [[],[],[]]
for i in range(3):
    min_sum_dist = 10**8
    for x1,y1 in clusters[i]:
        sum_10 = 0 #Растояние
        for x2,y2 in clusters[i]:
            sum_10 += dist([x1,y1],[x2,y2])
        if sum_10 < min_sum_dist:
            min_sum_dist = sum_10
            best_centr[i] = [x1,y1]
print(best_centr)
P_x = sum([x for x,y in best_centr]) / 3
P_y = sum([y for x , y in best_centr]) / 3
print(P_x * 10_000, P_y * 10_000)


# 8313.429500915556 16213.23920483777
# 2215.1447383158893 п  в.190128455895