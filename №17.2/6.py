# №6. В файле содержится последовательность натуральных чисел. Элементы последовательности могут принимать целые значения от 1 до 100 000 включительно. Определите количество троек элементов последовательности, в которых ровно два из элементов являются трёхзначными, а сумма элементов тройки не больше максимального элемента последовательности, оканчивающегося на 111. В ответе запишите через пробел количество найденных троек чисел, затем максимальную из сумм элементов таких троек. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
file = open("17.2/17.6.txt")
list = [int(line) for line in file]
sum_par = []
max_111 = max([x for x in list if x % 1000 == 111])
for i in range(len(list)-2):
    if ((len(str(list[i]))==3) + (len(str(list[i+1]))==3) + (len(str(list[i+2]))==3)) == 2 and sum(list[i:i+3]) <= max_111:
        sum_par.append(sum(list[i:i+3]))
print(len(sum_par), max(sum_par))

