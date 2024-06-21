with open('text18-11.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    punctuation_count = sum([1 for symbol in content if symbol in '.,:;!?'])

# Выводим содержимое файла и количество знаков препинания
print(content)
print('Количество знаков препинания:', punctuation_count)

# Разбиваем содержимое на отдельные строки
lines = content.split('\n')

# Находим строку наименьшей длины
shortest_line = min(lines, key=len)

# Создаем новый файл с строкой наименьшей длины
with open('shortest_line.txt', 'w', encoding='utf-8') as file:
    file.write(shortest_line)