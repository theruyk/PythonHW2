# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем 
# и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для 
# проверки своего кода используйте модуль fractions.

from fractions import Fraction

def fractions(fraction1, fraction2):
    fraction1 = Fraction(fraction1)
    fraction2 = Fraction(fraction2)

    sum_fractions = fraction1 + fraction2
    multiply_fractions = fraction1 * fraction2

    return sum_fractions, multiply_fractions


fraction_1 = input("Введите первую дробь a/b: ")
fraction_2 = input("Введите вторую дробь a/b: ")

sum_result, multiply_result = fractions(fraction_1, fraction_2)
print(f"Сумма: {sum_result}")
print(f"Произведение: {multiply_result}")
