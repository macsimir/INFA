#№3. В файле содержится последовательность из 10 000 целых положительных чисел. Каждое число не превышает 10 000. Определите и запишите в ответе сначала количество пар элементов последовательности, для которых произведение элементов делится без остатка на 74, затем максимальную из сумм элементов таких пар. В качестве пары рассматривается два элемента, идущие друг за другом. В ответ запишите целые числа через пробел: сначала количество, затем максимальное значение.

file = open('17/17.3.txt')
list = []
for line in file:
    list.append(int(line))
sum_par = []
for i in range(len(list)-1):
    if list[i] * list[i+1] % 74 == 0:
        sum_par.append(list[i] + list[i+1])
print(len(sum_par))
print(max(sum_par))