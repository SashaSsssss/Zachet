a=int(input("Введите A: "))
b=int(input("Введите B, B<A: "))
m=-1
if a <= b:
    print("Условие не выполняется A > B")
else:
    while a >= b:
        a = a-b
        m = a
if m !=- 1:
    print("Длина незанятой части = ",m)