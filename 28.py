input_file_name = input("Введите имя исходного файла: ")
output_file_name = input("Введите имя целевого файла: ")

try:
    with open(input_file_name, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    with open(output_file_name, "w", encoding="utf-8") as output_file:
        line_number = 1
        
        for line in lines:
            output_line = f"{line_number}: {line}"
            output_file.write(output_line)
            line_number += 1

        print("Файл", output_file_name, 'успешно создан.')
except FileNotFoundError:
    print("Ошибка: Файл не найден.")