def read_recipes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        cook_book = {}
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient = file.readline().strip().split(' | ')
                ingredient_name = ingredient[0]
                quantity = int(ingredient[1])
                measure = ingredient[2]
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
            file.readline() 
        return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
    
    return shop_list

file_path = 'recipes.txt'  
cook_book = read_recipes(file_path)
print(cook_book)

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
print(shop_list)