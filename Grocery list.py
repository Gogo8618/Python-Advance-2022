def shop_from_grocery_list(budget, grocery_list, *args):
    bought_products = []
    for product, price in args:

        if product not in grocery_list:
            continue
        elif budget < float(price):
            break
        else:
            bought_products.append(product)
            grocery_list.remove(product)
            budget -= float(price)

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(100, ['tomato', 'cola', 'chips', 'meat', 'chocolate'], ('cola', 15.8), ('chocolate', 30),
                             ('tomato', 15.85), ('chips', 50), ('meat', 22.99)))
