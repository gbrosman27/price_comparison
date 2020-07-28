class Item():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


def item_count():
    answer = input("Would you like to add an item?").lower()
    if answer == "yes":
        items = add_item_to_list()   
        item_count()     
    elif answer == "no":
        print("ok")
    else:
        print("I didn't recognize that.")
        item_count()        
        

def add_item_to_list():
    items_list = []
    name_of_item = input("What is the name of the item?")
    price_of_item = float(input("What is the price of the item?"))
    quantity_of_item = int(input("How many are you buying?"))
    new_item = Item(name_of_item, price_of_item, quantity_of_item)
    items_list.append(new_item)    
    return items_list

def total_cost(item):
    total = item.price * item.quantity
    print(f"The item's total cost is: ${total}.")
    return total


item_count()
