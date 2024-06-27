def find_max_sequence(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    max_length = 0
    current_length = 0
    x_count = 0

    for char in text:
        if char in ['I', 'U', 'V', 'W', 'X', 'U', 'Z']:
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

    if current_length > max_length:
        max_length = current_length

    return max_length


file_path = '313_24.txt'
print(find_max_sequence(file_path))