# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
num = randint(0, 1000)

while True:
  number = int(input("Введите число от 0 до 1000: "))
  if 0 <= number <= 1000:
    if number > num: 
      print("Mеньше")
    elif number < num:
      print("Больше")
    else: 
      print("Вы угадали загаданное число!")
      break
  else: print("Введите допустимое число!")