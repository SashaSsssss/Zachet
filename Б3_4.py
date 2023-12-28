a = int(input('Введите целое число A: '))
b = int(input('Введите целое число B, B>A: '))
 
sum_All = 0
sum_Chet = 0
sum_Nechet = 0
for i in range(a, b+1):
    sum_All+=i
    
    if i%2==0:
        sum_Chet+=i
    
    else:
        sum_Nechet+=i
print ('Сумма всех чисел', + sum_All) 
print ('Сумма чётных чисел', + sum_Chet)
print ('Сумма нечётных чисел', + sum_Nechet)