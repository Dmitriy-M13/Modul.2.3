num = int(input('введите число: '))
num_2 = int(input('введите в какую степень нужно возвести число от 0 до 7: '))

result = 1
for i in range(num_2):
    result *= num
    print(f"{num} в степени {num_2} равно {result}")
