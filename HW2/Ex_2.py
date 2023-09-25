# Напишите программу, которая получает целое число и возвращает его 
# шестнадцатеричное строковое представление. Функцию hex используйте для проверки 
# своего результата.

def to_hexadecimal(number):
    hexadecimal_str = hex(number)
    return hexadecimal_str

num = int(input("Введите целое число: "))
hexadecimal_result = to_hexadecimal(num)
print(f"Шестнадцатеричное представление: {hexadecimal_result}")
