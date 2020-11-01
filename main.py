from tkinter import *
from tkinter import font
from tkinter.font import BOLD, families


class Item:
    def __init__(self, name, price, servings):
        self.name = name
        self.price = price
        self.servings = servings


def item_count():
    items_list = []
    items = None
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
    try:
        name_of_item = input("What is the name of the item?  ")
        price_of_item = float(input("What is the price of the item?  "))
        servings_of_item = int(input("How many servings are in the item?  "))
        new_item = Item(name_of_item, price_of_item, servings_of_item)
        items_list.append(new_item)  
        return items_list  
    except ValueError:
        print("Enter valid input")
    

def cost_per_unit(item):
    cost_list = []
    for x in item:
        total = round(x.price / x.servings, 2)
        result = f"The {x.name} cost per serving is: ${total}."
        cost_list.append(result)
    gui_kinter(cost_list)

def gui_kinter(display_string_list):
    root = Tk()
    text = Text(root, spacing1=2, font=BOLD)
    # loop over the list and convert to string format with new line.
    convert_list = '\n\n'.join(map(str, display_string_list)) 
    text.insert(INSERT, convert_list)
    text.pack()
    root.mainloop()


if __name__ == "__main__":
    item_count()
