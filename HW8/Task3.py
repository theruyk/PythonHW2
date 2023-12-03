import logging
import argparse
from ast import literal_eval


logging.basicConfig(filename='error_task3.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')


class LotteryGame:
    def __init__(self, list1, list2):
        self.validate_list_content(list1, "list1")
        self.validate_list_content(list2, "list2")
        self.list1 = list1
        self.list2 = list2
    
    def validate_list_content(self, lst, list_name):
        if not all(isinstance(item, (int, float)) for item in lst):
            raise ValueError(f"{list_name} должен содержать только числа.")

    def compare_lists(self):
        matching_numbers = [num for num in self.list1 if num in self.list2]
        if not matching_numbers:
            print("Совпадающих чисел нет.")
            return []
        else:
            print(f"Совпадающие числа: {matching_numbers}")
            print(f"Количество совпадающих чисел: {len(matching_numbers)}")
            return matching_numbers

def parse_arguments():
    parser = argparse.ArgumentParser(description='Lottery Game')
    parser.add_argument('list1', help='First list of numbers', type=str)
    parser.add_argument('list2', help='Second list of numbers', type=str)
    return parser.parse_args()

def main():
    args = parse_arguments()
    try:
        list1 = literal_eval(args.list1)
        list2 = literal_eval(args.list2)
        game = LotteryGame(list1, list2)
        matching_numbers = game.compare_lists()
    except ValueError as e:
        logging.exception("Возникла ошибка: ")
        print(f"Ошибка: {e}")
# try:

#     list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
#     list2 = [9, 5, 6, 12, 14, "22", 17, 41, 8, 3]

#     game = LotteryGame(list1, list2)
#     matching_numbers = game.compare_lists()

# except ValueError as e:
#     logging.exception("Возникла ошибка: ")
#     print(f"Ошибка: {e}")

if __name__ == '__main__':
    main()

#python3 /Users/the_ryuk/Desktop/PythonHW2/HW8/Task3.py "[3, 12, 8, 41, 7, 21, 9, 14, 5, 30]" "[9, 5, 6, 12, 14, 22, 17, 41, 8, 3]"
#python3 /Users/the_ryuk/Desktop/PythonHW2/HW8/Task3.py "[3, 12, 8, 'text', 7]" "[9, 5, 6, 12, 14]"
