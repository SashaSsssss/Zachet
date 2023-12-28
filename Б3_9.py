def func(a):
    if a == 1:
        return "Один"
    elif a == 2:
        return "Два"
    elif a == 3:
        return "Три"
    elif a == 4:
        return "Четыре"
    elif a == 5:
        return "Пять"
    elif a == 6:
        return "Шесть"
    elif a == 7:
        return "Семь"
    elif a == 8:
        return "Восемь"
    elif a == 9:
        return "Девять"
    elif a == 10:
        return "Десять"
    elif a == 11:
        return "Одиннадцать"
    elif a == 12:
        return "Двенадцать"
    else :
        return ""
if __name__ == "__main__":
    a = int(input("Введите число: "))
    print(func(a))