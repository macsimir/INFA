# №8. В файле содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от -100 О00 до 100 000 включительно. Определите количество троек элементов последовательности, в которых не более двух чисел являются пятизначными, а сумма элементов тройки не менее минимального элемента последовательности, оканчивающегося на 600. В ответе запишите через пробел количество найденных троек чисел, затем минимальную из сумм элементов таких троек. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
file = open("17.2/17.8.txt")
list = [int(line) for line in file]
sum_par = []
min_600 = min([x for x in list if abs(x) %1000 ==600])
for i in range(len(list)-3):
    if ((len(str(list[i]))==5)+(len(str(list[i+1]))==5)+(len(str(list[i+2]))==5))== 2 and sum(list[i:i+3]) >= min_600:
        sum_par.append(sum(list[i:i+3]))
print(len(sum_par),min(sum_par))


# f= open("17.2/17.8.txt")
# a = [int(s) for s in f]
# min600 = min([x for x in a if abs(x) % 1000 == 600])
# sum_troyki = []
# for i in range(len(a) - 2):
#     if ((len(str(abs(a[i]))) == 5) + (len(str(abs(a[i + 2]))) == 5)) <= + (len(str(abs(a[i + 1]))) == 5) == 2 and sum(a[i:i + 3]) >= min600:
#         sum_troyki.append(sum(a[i:i + 3]))
# print(len(sum_troyki), min(sum_troyki))