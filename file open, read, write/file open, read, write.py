from pathlib import Path

with open('recipes.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        recipe_name = line.strip()
        ingredient_count = int(f.readline())
        ingredients = []
        for i in range(ingredient_count):
            ingr = f.readline().strip()
            name, amount, measure = ingr.split(' | ')
            ingredients.append({
                'name': name,
                'amount': int(amount),
                'measure': measure
            })
        f.readline()
        cook_book[recipe_name] = ingredients

# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for dish, ingr in cook_book.items():
        if dish in dishes:
            for ingredient in ingr:
                sub_dict = {}
                name = ingredient['name']
                amount = ingredient['amount'] * person_count
                measure = ingredient['measure']
                sub_dict['measure'] = measure
                sub_dict['amount'] = amount
                if name not in shopping_list.keys():
                    shopping_list[name] = sub_dict
                else:
                    sub_dict['amount'] += amount
                    shopping_list[name] = sub_dict
    print(shopping_list)

# get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)


with open('1.txt', 'r') as f, open('2.txt', 'r') as d, open ('3.txt', 'r') as a, open('4.txt', 'w+') as s:

    main_list = [f, d, a]
    main_dict = {}
    for file in main_list:
        res = file.readlines()
        main_dict[file.name] = [str(len(res)), *res]

    sorted_list = sorted(main_dict.items(), key=lambda x:x[1][1], reverse=True)

    for file in sorted_list:
            for line in file:
                if isinstance(line, str):
                    s.write(line+'\n')
                if isinstance(line, list):
                    for element in line:
                        s.write(element+'\n')


