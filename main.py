import tkinter as tk


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
        if answer == "yes" or answer == "y":
            items = add_item_to_list(items_list)   
        elif answer == "no" or answer == "n":
            print("ok")
            break
        else:
            print("I didn't recognize that.")
    cost_per_unit(items)
        

def add_item_to_list(items_list):
    try:
        name_of_item = input("What is the name of the item?  ")
        price_of_item = float(input("What is the price of the item? (x.xx)  "))
        servings_of_item = int(input("How many servings are in the item? (x)  "))
        new_item = Item(name_of_item, price_of_item, servings_of_item)
        items_list.append(new_item)  
        return items_list  
    except ValueError:
        print("Enter valid input")
    

def cost_per_unit(item):
    cost_list = []
    for x in item:
        total = format(x.price / x.servings, ".2f")
        result = f"The {x.name} cost per serving is: ${total}"
        cost_list.append(result)
    gui_kinter(cost_list)


def gui_kinter(display_string_list):
    root = tk.Tk()    
    # loop over the list and convert to string format with new line.
    convert_list = '\n\n'.join(map(str, display_string_list)) 
    label = tk.Label(root, text=convert_list, fg="blue", font="Arial 16 bold")
    label.pack(fill=tk.X, padx=10, pady=10)
    root.mainloop()


if __name__ == "__main__":
    item_count()
