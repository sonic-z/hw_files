import os

file_path = os.path.join(os.getcwd(), 'recipes.txt')
cook_book = {}

with open(file_path, encoding='utf8') as f:
    for line in f:
        if line.strip() != '':
            if '|' not in line:
                if not line.strip().isdigit():
                    current_recipe = line.strip()
                    cook_book.setdefault(current_recipe, [])
            elif '|' in line:
                splitted_line = line.split('|')
                if len(splitted_line) == 3 and len(current_recipe) > 0:
                    ingredient = {'ingredient_name': splitted_line[0].strip(), 'quantity': splitted_line[1].strip(), 'measure': splitted_line[2].strip()}
                    cook_book[current_recipe].append(ingredient)
        else:
            current_recipe = ''

def get_shop_list_by_dishes(dishes:list, person_count:int):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = int(ingredient['quantity'])
            measure = ingredient['measure']
            if ingredient_name not in shop_list:
                shop_list.setdefault(ingredient_name, {'quantity': quantity*person_count, 'measure': measure})
            else:
                old_quantity = shop_list[ingredient_name][quantity]
                shop_list[ingredient_name][quantity] = old_quantity + quantity*person_count
    return shop_list

get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 3)