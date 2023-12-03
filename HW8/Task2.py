# Задача 2
import argparse
from ast import literal_eval
import logging

logging.basicConfig(filename='error_task2.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class InvalidTextError(Exception):
    """Исключение возникает, когда текст не является строкой или пустой."""
    pass

class InvalidNumberError(Exception):
    """Исключение возникает, когда число не является положительным целым числом или числом с плавающей запятой ."""

class Archive:
    _instance = None
    archive_text = []
    archive_number = []

    def __new__(cls, text, number):
            if not text or not isinstance(text, str):
                raise InvalidTextError("Текст должен быть непустой строкой")
            if not isinstance(number, (int,float)):
                raise InvalidNumberError("Число не является целым числом или числом с плавающей запятой ")
            if number < 0:
                raise InvalidNumberError("Число должно быть положительным")
            if cls._instance is None:
                cls._instance = super(Archive, cls).__new__(cls)
            cls.archive_text.append(text)
            cls.archive_number.append(number)
            return cls._instance

    def __init__(self, text, number):
        self.text = text
        self.number = number

    def __str__(self):
        return (f"Text is {self.text} and number is {self.number}. "
                f"Also {self.archive_text} and {self.archive_number}")

    def __repr__(self):
        return f"Archive('{self.text}', {self.number})"

def parse_arguments():
    parser = argparse.ArgumentParser(description='Archive Management')
    parser.add_argument('text', type=str)
    parser.add_argument('number', type=float)
    return parser.parse_args()

def main():
    args = parse_arguments()
    try:
        archive = Archive(args.text, args.number)
        print(archive)
    except InvalidTextError as e:
        logging.exception("Текст должен быть непустой строкой")
        print(f"Ошибка: {e}")
    except InvalidNumberError as e:
        logging.exception("Число не является целым числом или числом с плавающей запятой ")
        print(f"Ошибка: {e}")


# try:
#     archive1 = Archive("Запись 1", 42)
#     print(archive1)

#     archive2 = Archive("Запись 2", 3.14)
#     print(archive2)
    
#     archive3 = Archive("Запись 3", -3.14)
#     print(archive2)
# except InvalidNumberError as e:
#     logging.exception("Возникла ошибка: ")
#     print(f"Ошибка: {e}")
# try:
#     archive4 = Archive(None, 100)
#     print(archive4)

#     archive5 = Archive('', 100)
#     print(archive4)

# except InvalidTextError as e:
#     logging.exception("Возникла ошибка: ")
#     print(f"Ошибка: {e}")

if __name__ == '__main__':
    main()

#python3 /Users/the_ryuk/Desktop/PythonHW2/HW8/Task2.py "Some text" 123.45
#python3 /Users/the_ryuk/Desktop/PythonHW2/HW8/Task2.py "Some text" -2