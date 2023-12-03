# На вход подается словарь со списком вещей для похода в качестве ключа и их 
# массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную 
# грузоподъёмность.
# Результат должен быть в виде словаря с вещами в рюкзаке:{предмет:вес}



def backpack(items, max_weight):
    full_backpack = {}
    current_weight = 0

    sorted_items = dict(sorted(items.items(), key=lambda x: x[1]))

    for key, value in list(sorted_items.items()):  
        if current_weight + value <= max_weight:
            full_backpack[key] = value
            current_weight += value
            items.pop(key)  

    return full_backpack

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1,

}
max_weight = 1.0

print(backpack(items, max_weight))

