# Напишите функцию принимающую на вход только ключевые параметры и возвращающую 
# словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def creation_dict(**kwargs):
  new_dict = {}
  for key, value in kwargs.items():
    try:
      hash(key)
      new_dict[value] = key
    except TypeError:
      new_dict[str(value)] = key
  return new_dict

print(creation_dict(age=25, name="John", my_list = [1, 2, 3]))