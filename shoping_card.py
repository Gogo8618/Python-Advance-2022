def shopping_cart(*args):
    cart = {'Pizza': [], 'Soup': [], 'Dessert': []}

    for tuple_ in args:
        meal = tuple_[0]
        product = tuple_[1]

        if tuple_ == 'Stop':
            break
        if meal == 'Pizza' and len(cart['Pizza']) > 4:
            continue
        elif meal == 'Soup' and len(cart['Soup']) > 3:
            continue
        elif meal == 'Dessert' and len(cart['Dessert']) > 2:
            continue
        if product not in cart[meal]:
            cart[meal].append(product)
    for v in cart.values():
        if len(v) > 0:
            break
        else:
            return "No products in the card!"
    sort_product = sorted(cart.items(), key=lambda a: (-len(a[1]), a[0]))
    result = ''
    for meals in sort_product:
        result += f'{meals[0]}:\n'
        sort_value = sorted(meals[1])
        for v in sort_value:
            result += f"- {v}\n"
    return result


print(shopping_cart(('Pizza', 'ham'), ('Soup', 'carrots'), ('Pizza', 'cheese'), ('Pizza', 'flours'), ('Dessert', 'milk'),
                    ('Pizza', 'mushrooms'), ('Pizza', 'tomatoes'), 'Stop',))
