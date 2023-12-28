def gipotenuza():
    C = (katet_1 ** 2 + katet_2 ** 2) ** 0.5
    return(C)

print('Введите длину первого катета: ')
katet_1 = float(input())
print(f'Введите длину второго катета: ')
katet_2 = float(input())

print(gipotenuza())