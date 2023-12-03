# На вход подается словарь со списком вещей для похода в качестве ключа и их 
# массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную 
# грузоподъёмность.
# Результат должен быть в виде словаря с вещами в рюкзаке:{предмет:вес}
# Верните все возможные варианты комплектации рюкзака.


# def backpack(items, max_weight, current_combination=None):
#     if current_combination is None:
#         current_combination = {}

#     combinations = []

#     for item, weight in items.items():
#         if item not in current_combination and sum(current_combination.values()) + weight <= max_weight:
#             new_combination = dict(current_combination)
#             new_combination[item] = weight

#             combinations.append(new_combination)

#             sub_combinations = backpack(items, max_weight, new_combination)
#             combinations.extend(sub_combinations)

#     return combinations

# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1,
# }

# max_weight = 1.0

# result = backpack(items, max_weight)

# for combination in result:
#     print([combination])

from itertools import combinations

def get_combinations(items, max_weight):
    result = []
    for r in range(1, len(items) + 1):
        for combo in combinations(items.items(), r):
            combined_dict = dict(combo)
            total_weight = sum(combined_dict.values())
            if total_weight <= max_weight:
                result.append(combined_dict)
    return result

# Пример использования
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}

max_weight = 1.0

result = get_combinations(items, max_weight)

# Вывод результата
for res in result:
    print(res)

