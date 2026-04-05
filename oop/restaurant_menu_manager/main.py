import json

class MenuItem:
    def __init__(self, name: str, category: str, price):
        self.name =  name
        self.category = category
        self.price = price

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}, Price: ${self.price:.2f}"

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "price": f'{self.price:.2f}'
        }


class MenuManager:
    def __init__(self):
        self.menu_items = {}

    def add_item(self, item: MenuItem):
        if not item.category in self.menu_items:
            self.menu_items[item.category] = {}
        self.menu_items[item.category][item.name] =  item
        print(f"Added new item: {item.name} to the category: {item.category} menu.")
        
    def remove_item(self, name: str, category: str):
        if category in self.menu_items:
            del self.menu_items[category][name]
            print(f"The item: {name} has been remove of the menu.")
        else:
            print(f"Not found the item: {name} in the menu.")

    def list_items(self):
        for category, item in self.menu_items.items():
            for item in item.values():
                print(f'{category}: {item}')

    def update_item_price(self, name:str, category: str, new_price: float):
        if category in self.menu_items and name in self.menu_items[category]:
            self.menu_items[category][name].price = new_price
            print(f'Change new price: ${new_price:.2f} to the item: {name}')
        else:
            print('The item not exist.')

    def list_items_by_category(self, category):
        if category in self.menu_items:
            print(category.upper())
            for item in self.menu_items[category]:
                print(f'{"":2}- {item}')

    def save_to_file(self, filename: str):
        with open(filename, 'w') as file:
            json.dump(self.menu_items, file, default=to_dict_func, indent=4)

    def load_from_file(self, filename):
        with open(filename, 'r') as read_file:
            items = json.load(read_file)
            for name, category, price in items.items():
                self.add_item(
                    {
                        "name": name, 
                        "category": category, 
                        "price": price
                    })
            print('Add the items correctly.')


def to_dict_func(obj):
    return obj.to_dict()


tortilla = MenuItem('Tortilla', 'Complements', 0.20)
totopos = MenuItem('Totopos', 'Complements', 1.0)
salsa = MenuItem('Salsa', 'Complements', 0.50)
coffe = MenuItem('Coffe', 'Berevage', 3.50)
soda = MenuItem('Soda', 'Berevage', 3.0)
sandwitch = MenuItem('Sandwitch', 'Snack', 2.00)
french_fries = MenuItem('French Fries', 'Snack', 1.50)

print(tortilla)
print(coffe)
print(sandwitch)

print('*' * 10)

menu = MenuManager()
menu.add_item(tortilla)
menu.add_item(totopos)
menu.add_item(salsa)
menu.add_item(coffe)
menu.add_item(sandwitch)
menu.add_item(soda)
menu.add_item(french_fries)

print("*" * 10)

new_item = MenuItem('Salad', 'Complements', 2.0)
menu.add_item(new_item)
menu.remove_item('Salad', 'Complements')
menu.list_items()

print("*" * 10)

menu.update_item_price('Tortilla', 'Complements', 1)
menu.update_item_price('Soda', 'Berevage', 2.4)

print("*" * 10)

menu.list_items()

print("*" * 10)

menu.list_items_by_category('Complements')

print("*" * 10 )

print(tortilla.to_dict())
print(totopos.to_dict())
print(soda.to_dict())

print()

menu.save_to_file('data.txt')

print()

menu.load_from_file("json_data.json")








