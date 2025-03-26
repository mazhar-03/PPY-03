def check_stocks():
    stock = {}
    print("Enter stock information. If you would like to exit, write 'done': ")
    while True:
        product = input("Product name: ")
        if product == "done":
            break
        quantity = input(f"Quantity of {product}: ")
        if not quantity.isdigit():
            print("Enter valid number")
            continue
        if product in stock:
            stock[product] += int(quantity)
            print("Product added.")
        else:
            stock[product] = int(quantity)
            print("Product saved.")

    print("\nEnter customer orders. If you would like to exit, write 'done': ")
    while True:
        order_product = input("Ordered product name: ")
        if order_product == "done":
            break
        if order_product not in stock.keys():
            print(f"No stocks available for {order_product}\n")
            continue

        order_quantity = input(f"Order quantity of {order_product}: ")
        if not order_quantity.isdigit():
            print("Enter valid number\n")
            continue
        order_quantity = int(order_quantity)

        if order_product in stock and stock[order_product] >= order_quantity:
            stock[order_product] -= order_quantity
            print(f"{order_quantity} {order_product} order fulfilled.")
        else:
            print("Order cant be fulfilled. Not enough stocks!")

    print("\nStock Availability: ")
    for item, quantity in stock.items():
        print(f"{item}: {quantity}")


check_stocks()
