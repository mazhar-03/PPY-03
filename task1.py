sales = {}

while True:
    answer = input("Write the product (name, price, quantity). If you would like to exit, write 'done': ")

    if answer == 'done':
        break

    data = answer.split(',')
    if len(data) == 3:
        product, price, quantity = data[0].strip(), data[1].strip(), data[2].strip()
        if price.replace('.', '').isdigit() and quantity.isdigit():
            price, quantity = float(price), int(quantity)
            if product in sales:
                sales[product] += price * quantity
                print(f"Product {product} added successfully")
            else:
                sales[product] = price * quantity
                print(f"Product {product} created successfully")
        else:
            print("Invalid input.Price is number quantity is integer")
    else:
        print("Invalid format")

print("Sales Revenue Report:")
for product in sales:
    print(f"{product}: ${sales[product]}")
