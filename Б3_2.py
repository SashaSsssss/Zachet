a = int(input('Введите число A: '))
b = int(input('Введите число B>A: '))
if a>b:
    print("Число A больше числа B!")
else:
    sum = 0
    for i in range (a,b):
        print(i, end=' ')
        sum = sum + 1
    print(b)
    sum = sum + 1
    print(f"Количество чисел в последовательности = {sum}")