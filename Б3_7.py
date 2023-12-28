a = float(input("Введите A = "))
b = float(input("Введите B = "))
c = float(input("Введите C = "))
k = 0
while a - c >= 0:
    a -= c
    b1=b
    while b1 - c >= 0:
            b1 -= c
            k += 1
print("Количествово квадратов =",k)