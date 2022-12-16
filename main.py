def get_shop_list_by_dishes(dishes, person_count):
    ingredients_dishes = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            ingr_dish = ingr['ingredient_name']
            quant_dish = int(ingr['quantity'])
            measure_dish = ingr['measure']
            quant_dish = quant_dish * person_count
            if ingr_dish in ingredients_dishes:
                ingredients_dishes[f'{ingr_dish}']['quantity'] = int(
                    ingredients_dishes[f'{ingr_dish}']['quantity']) + quant_dish
            else:
                ingredients_dishes[f'{ingr_dish}'] = {'measure': f'{measure_dish}', 'quantity': f'{quant_dish}'}

    return ingredients_dishes


with open('recept.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        recept_name = line.strip()
        ingredients_quantity = int(f.readline())
        ingredients = []
        for i in range(ingredients_quantity):
            ingredient = f.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book.update({
            f'{recept_name}': ingredients
        })
print(cook_book)
print()
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))