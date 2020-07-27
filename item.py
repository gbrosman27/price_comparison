class Item():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

items_list = []

def add_item_to_list():
    name_of_item = input("What is the name of the item?")
    price_of_item = float(input("What is the price of the item?"))
    quantity_of_item = int(input("How many are you buying?"))
    new_item = Item(name_of_item, price_of_item, quantity_of_item)
    return new_item

def total_cost(item):
    total = item.price * item.quantity
    return total


items_list.append(add_item_to_list())
print(f"The first item's total cost is: ${total_cost(items_list[0])}.")

items_list.append(add_item_to_list())
print(f"The second item's total cost is: ${total_cost(items_list[1])}.")
