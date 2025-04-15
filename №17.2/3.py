# №3. Файл содержит последовательность неотрицательных целых чисел, не превышающих 10000. Назовём парой два идущих подряд элемента последовательности. Определите количество пар, в которых ровно один из двух элементов делится на 5, а также хотя бы один из двух элементов меньше среднего арифметического всех чётных элементов последовательности. В ответе запишите два числа через пробел: сначала количество найденных пар, а затем - максимальную сумму элементов таких пар.

file = open("17.2/17.3.txt")
list = [int(line) for line in file]
sum_par = []
chet_element = []
for x in range(len(list)-1):
    if list[x] // 2:
        chet_element.append(x)
sred_element = sum(chet_element) // len(chet_element)


for i in range(len(list)-1):
    if (list[i] % 5 == 0 and list[i+1] % 5 != 0) or  (list[i] % 5 != 0 and list[i+1] % 5 == 0):
        if list[i] < sred_element or list[i+1] <sred_element:
            sum_par.append(list[i]+list[i+1])
print(len(sum_par),max(sum_par))
