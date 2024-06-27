def find_max_sequence(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    max_length = 0
    current_length = 0
    t_count = 0

    for char in text:
        if char in ['T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            current_length += 1
            if char == 'T':
                t_count += 1
            if t_count > 100:
                current_length = 0
                t_count = 0
        else:
            if current_length > max_length and t_count == 100:
                max_length = current_length
            current_length = 0
            t_count = 0

    if current_length > max_length and t_count == 100:
        max_length = current_length

    print(f"Максимальная длина непрерывной подпоследовательности с 100 символами 'T': {max_length}")
    return max_length


file_path = '24_2024.txt'
find_max_sequence(file_path)
