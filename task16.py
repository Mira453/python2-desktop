def calculate_order(pricelist, order):
    
    pricelist = [(item[0].strip().lower(), item[1], item[2]) for item in pricelist]
    order = [(item[0].strip().lower(), item[1]) for item in order]

    
    updated_pricelist = list(pricelist)
    total_cost = 0  

    for item_name, item_qty in order:
        
        for i, (price_name, price_cost, price_qty) in enumerate(updated_pricelist):
            if price_name == item_name:
                if item_qty > price_qty:
                    return -1  
                total_cost += item_qty * price_cost
                
                updated_pricelist[i] = (price_name, price_cost, price_qty - item_qty)
                break
        else:
            return -2  

    return total_cost, updated_pricelist


pricelist = [
    ["ХЛІБ", 20, 50],
    ["МОЛОКО", 30, 100],
    ["ЯЙЦЯ", 10, 200]
]


order = (
    ("хліб", 2),
    ("молоко", 1),
    ("яйця", 12)
)


result = calculate_order(pricelist, order)


if isinstance(result, tuple):
    total_cost, updated_pricelist = result
    print("Загальна вартість замовлення:", total_cost)
    print("Оновлений прейскурант:")
    for item in updated_pricelist:
        print(item)
else:
    if result == -1:
        print("Помилка: запитувана кількість перевищує наявну!")
    elif result == -2:
        print("Помилка: товару немає в прейскуранті!")