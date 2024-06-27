def max_continuous_subsequence(filename):
    with open(filename, 'r') as file:
        text = file.read().strip()

    max_length = 0
    current_length = 0
    x_count = 0

    for char in text:
        if char == 'X':
            x_count += 1
            if x_count > 140:
                current_length = 0
                x_count = 1
            else:
                current_length += 1
                max_length = max(max_length, current_length)
        else:
            current_length += 1
            max_length = max(max_length, current_length)

    return max_length

# Пример использования
filename = '313_24.txt'
result = max_continuous_subsequence(filename)
print(f"Максимальная длина непрерывной подпоследовательности: {result}")