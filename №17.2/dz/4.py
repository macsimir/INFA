# В файле 17.10.txt содержится последовательность из 10000 целых положительных чисел.Каждое число не превышает 10 000. Определите и запишите в ответе без пробела сначала количество пар элементов последовательности, в которых запись ровно одного элемента заканчивается цифрой 6, а сумма квадратов элементов пары меньше, чем квадрат наибольшего из элементов последовательности, запись которых заканчивается цифрой 6, затем максимальную сумму квадратов элементов таких пар. В качестве пары рассматривается два элемента, идущие друг за другом.
file = open("17.2/dz/dz4.txt")
list = [int(line)for line in file]
sum_par = []
max_par = max([list[i]**2 for i in range(len(list)-1) if list[i] % 10 == 6])
for i in range(len(list)-1):
    if ((list[i] % 10 == 6)+(list[i+1] % 10 == 6))==1 and list[i]**2 + list[i+1]**2 <max_par:
        sum_par.append(list[i]**2 + list[i+1]**2)
print(len(sum_par),max(sum_par))
        
