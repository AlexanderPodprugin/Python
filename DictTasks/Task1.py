"""
Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
"""
result = {}
for i in range(1, 10):
    result[i] = i**3

print(result)