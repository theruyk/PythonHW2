from datetime import datetime
import logging
import argparse

logging.basicConfig(filename='error_task1.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class MyStr(str):
    def __new__(cls, value, author):
        if not isinstance(value, str) or value.isdigit():
            raise ValueError("Value должно быть строкой, не содержащей только цифры")
        if not isinstance(author, str) or author.isdigit():
            raise ValueError("Author должен быть строкой, не содержащей только цифры")
        instance = super(MyStr, cls).__new__(cls, value)
        instance.value = value
        instance.author = author
        instance.time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return instance

    def __str__(self):
        return f"{self.value} (Автор: {self.author}, Время создания: {self.time})"

    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author}')"

def parse_arguments():
    parser = argparse.ArgumentParser(description='Create MyStr object with value and author')
    parser.add_argument('value', type=str, help='The value of the MyStr object')
    parser.add_argument('author', type=str, help='The author of the MyStr object')
    return parser.parse_args()

def main():
    args = parse_arguments()
    try:
        my_string = MyStr(args.value, args.author)
        print(my_string)
    except ValueError as e:
        logging.exception("Возникла ошибка: ")
        print(f"Возникла ошибка: {e}")


# try:
#     event = MyStr("Завершилось тестирование", "John")
#     print(event)

#     my_string = MyStr("Пример текста", "Иван")
#     print(my_string)

#     my_string = MyStr(2, "Николай") 
#     print(repr(my_string))

# except ValueError as e:
#     logging.exception("Value и author должны быть строками")
#     print(f"Возникла ошибка: {e}")

if __name__ == '__main__':
    main()

#python3 /Users/the_ryuk/Desktop/PythonHW2/HW8/Task1.py "Текст события" "Имя автора"
#python3 /Users/the_ryuk/Desktop/PythonHW2/HW8/Task1.py 123 456
