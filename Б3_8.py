def funkcia(a):
    m=a/140
    m=m*15
    print('Цена поездки', round(240+m, 2))

print('Введите расстояние в км:')
b=int(input())
funkcia(b)