#Текстовый файл состоит из символов I, U, V, W, X, U и Z.
#Определите в прилагаемом файле максимальное количество идущих подряд символов (длину непрерывной подпоследовательности),
#среди которых символ Х встречается не более 140 раз.

def find_max_sequence(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    max_length = 0
    current_length = 0
    x_count = 0

    for char in text:
        if char in ['T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            current_length += 1
            if char == 'X':
                x_count += 1
            if x_count > 140:
                current_length = 0
                x_count = 0
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
            x_count = 0

    return max(max_length, current_length)

