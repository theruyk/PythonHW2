# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — 
# функции. Дополнительно сохраняйте все операции поступления и снятия средств 
# в список.

def main():
    balance = 0
    count = 0
    operations = []
    def replenishment():
      nonlocal balance
      nonlocal count
      nonlocal operations
      amount = int(input("Введите сумму для пополнения (кратную 50): "))
      if amount % 50 != 0:
        print("Сумма должна быть кратной 50")
      else:
          balance += amount
          count += 1
          operations.append(f'+{amount}- Пополнение')

    def withdraw():
      nonlocal balance
      nonlocal count
      nonlocal operations
      amount = int(input("Введите сумму для снятия (кратную 50): "))
      if amount % 50 != 0:
        print("Сумма должна быть кратной 50")
      elif amount > balance:
        print("Недостаточно средств на счете.")
      else:
        if count % 3 == 0:
          balance -= amount
          tax = min(max(amount * 0.015, 30), 600)
          balance -= tax
          operations.append(f'-{tax} - Налог')
          count += 1
          print(f"Снято {amount} с учетом налога {tax}")
        else:
            balance -= amount
            count += 1
            operations.append(f'-{amount} - Снятие')
            print(f"Снято {amount}")

    while True:
        print(f"Текущий баланс: {balance} ")
        print(f'История операций: {operations}')

        operation = input("Выберите действие (1 - Пополнить, 2 - Снять, 3 - Выйти): ")

        if operation == "1":
          replenishment()


        elif operation == "2":
          withdraw()
            

        elif operation == "3":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")

        if balance > 5000000:
            tax = balance * 0.1
            balance -= tax
            operations.append(f'-{tax} - Налог')
            print(f"Удержан налог на богатство: {tax}")

main()