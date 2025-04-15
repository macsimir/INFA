# Файл 17_03.txt содержит последовательность неотрицательных целых чисел, не превышающих 10000. Назовём парой два идущих подряд элемента последовательности. Определите количество пар, в которых только один из двух элементов делится на 7, а другой больше среднего арифметического всех нечетных элементов последовательности. В ответе запишите два числа: сначала количество найденных пар, а затем, без пробела, минимальную сумму элементов таких пар.
# Например, в последовательности (1 7 6 8 14) есть две подходящих пары: (7 6) и (8 14), в ответе для этой последовательности надо записать числа 2 и 13.
# file = open('17.2/dz/dz3.txt')
# list = [int(line)for line in file]
# sum_par = []
# nechet_4 = [x for x in list if x% 2 != 0]
# nechet_4 = sum(nechet_4) / len(nechet_4)
# for i in range(len(list)-1):
#     if (list[i] % 7 ==0  and list[i+1] > nechet_4 and list[i+1]% 2 !=0) or (list[i] > nechet_4 and list[i+1] % 7 ==0 and list[i+1]% 2 !=0   ):
#         sum_par.append(list[i]+ list[i+1])
# print(len(sum_par),min(sum_par),sep='')


# file = open('17.2/dz/dz3.txt')
# list_ = [int(line) for line in file]
# sum_par = []
# nechet_4 = [x for x in list_ if x % 2 != 0]
# nechet_4 = sum(nechet_4) / len(nechet_4)
# for i in range(len(list_)-1):
#     if ((list_[i] % 7 == 0 and list_[i+1] > nechet_4 and list_[i+1] % 7 != 0) or 
#         (list_[i] > nechet_4 and list_[i] % 7 != 0 and list_[i+1] % 7 == 0)):
#         sum_par.append(list_[i] + list_[i+1])
# print(len(sum_par), min(sum_par), sep='')


file = open("17.2/dz/dz3.txt")
list = [int(line)for line in file ]
sum_par = []
nechet_4 = [x for x in list if x % 2 != 0]
nechet_4 = sum(nechet_4) / len(nechet_4)
for i in range(len(list)-1):
    if ((list[i] % 7 ==0) and (list[i+1] % 7 != 0) and (list[i+1] > nechet_4)) or  ((list[i] % 7 !=0) and (list[i+1] % 7 == 0) and (list[i] > nechet_4)):
        sum_par.append(list[i]+list[i+1])
print(len(sum_par),min(sum_par), sep='')