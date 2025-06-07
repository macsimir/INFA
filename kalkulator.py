# Чтение данных из файла
with open('dz_17/5.txt', 'r') as file:
    numbers = list(map(int, file.readlines()))

# Вычисление суммы всех положительных элементов
sum_pos = sum(x for x in numbers if x > 0)

count = 0
min_abs_sum = None

# Перебор всех троек подряд идущих элементов
for i in range(len(numbers) - 2):
    a, b, c = numbers[i], numbers[i+1], numbers[i+2]
    current_triple = [a, b, c]
    min_val = min(current_triple)
    max_val = max(current_triple)
    
    # Проверка условия
    if min_val * max_val > sum_pos:
        count += 1
        current_sum = a + b + c
        abs_sum = abs(current_sum)
        if min_abs_sum is None or abs_sum < min_abs_sum:
            min_abs_sum = abs_sum

print(f"{count}{min_abs_sum}")