class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


def item_count():
    items_list = []
    while True:
        answer = input("Would you like to add an item (yes or no)?  ").lower()
        if answer == "yes":
            items = add_item_to_list(items_list)   
        elif answer == "no":
            print("ok")
            break
        else:
            print("I didn't recognize that.")
    cost_per_unit(items)
        

def add_item_to_list(items_list):
    name_of_item = input("What is the name of the item?  ")
    price_of_item = float(input("What is the price of the item?  "))
    quantity_of_item = int(input("How many servings are in the item?  "))
    new_item = Item(name_of_item, price_of_item, quantity_of_item)
    items_list.append(new_item)    
    return items_list
    

def cost_per_unit(item):
    for x in item:
        total = round(x.price / x.quantity, 2)
        print(f"The {x.name} cost per unit is: ${total}.")


if __name__ == "__main__":
    item_count()
