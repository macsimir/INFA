# В файле содержится последовательность целых чисел из диапазона [-10000, 10000]. Определите количество троек элементов, в которых хотя бы один элемент отрицательный, а также минимальную сумму элементов таких троек. В качестве тройки рассматривается три элемента, идущие друг за другом. В ответ запишите целые числа без пробела и иных разделителей: сначала количество, затем минимальное значение суммы.

file = open("17/dz/3.txt")
list = [int(line)for line in file]
sum_par = []
for i in range(len(list)-2):
    if list[i] < 0 or list[i+1] < 0 or list[i+2] < 0:
        sum_par.append(list[i]+list[i+1]+list[i+2])
print(len(sum_par),min(sum_par))