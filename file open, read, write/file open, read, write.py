import os

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

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)


with open('1.txt', 'r') as f, open('2.txt', 'r') as d, open ('3.txt', 'r') as a, open('4.txt', 'w+') as s:
    main_list = []

    res = f.readlines()
    res_len = str(len(res))
    res_name = '1.txt'
    res.insert(0, res_name)
    res.insert(1, res_len)

    res_2 = d.readlines()
    res_2_len = str(len(res_2))
    res_2_name = '2.txt'
    res_2.insert(0, res_2_name)
    res_2.insert(1, res_2_len)

    res_3 = a.readlines()
    res_3_len = str(len(res_3))
    res_3_name = '3.txt'
    res_3.insert(0, res_3_name)
    res_3.insert(1, res_3_len)

    main_list.append(res)
    main_list.append(res_2)
    main_list.append(res_3)
    main_list.sort(key=len)

    for element in main_list:
        for line in element:
            s.write(line+'\n')

