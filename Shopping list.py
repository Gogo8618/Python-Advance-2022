def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."
    basket = {}

    for product, value in kwargs.items():
        price, quantity = value
        total_price = price * quantity
        if total_price <= budget:
            basket[product] = total_price
            budget -= total_price
        if len(basket) == 5 or budget == 0:
            break
    result = ''

    for key, value in basket.items():
        if value:
            result += f"You bought {key} for {value:.2f} leva.\n"
    return result


print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10), ))
