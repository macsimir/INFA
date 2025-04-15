# В файле содержится последовательность целых чисел из диапазона [-10000, 10000]. Определите количество пар элементов, из которых хотя бы одно число – это квадрат натурального числа, а также максимальную сумму элементов таких пар. В качестве пары рассматривается два элемента, идущие друг за другом. В ответ запишите целые числа без пробела: сначала количество, затем максимальное значение.
import math

file = open("17/dz/4.txt")
numbers = [int(line) for line in file]

sum_par = []
for i in range(len(numbers) - 1):
    if numbers[i] >= 0 and math.sqrt(numbers[i]) % 1 == 0 or numbers[i+1] >= 0 and math.sqrt(numbers[i+1]) % 1 == 0:
        sum_par.append(numbers[i] + numbers[i+1])

print(len(sum_par), max(sum_par) if sum_par else 0)