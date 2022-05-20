import json

import menu as menu


class Pizzeria:

    def __init__(self):
        self.menu = None

    def load_menu(self):
        with open('menu.json', 'r') as f:
            self.menu = json.load(f)
            return self.menu

    def save_menu(self):
        with open('menu.json', 'w') as f:
            json.dump(self.menu, f)

    def add_pizza(self, name, price):
        self.load_menu()
        if name in self.menu.keys():
            print('already there is')
        else:
            self.menu[name] = price
        self.save_menu()

    def remove_pizza(self, name):
        self.load_menu()
        if name in self.menu.keys():
            print('delete')
            del self.menu[name]
        else:
            print('no pizza')
        self.save_menu()

    def order_pizza(self):
            self.load_menu()
            order = []
            cost = 0
            while True:
                q1 = input('continue?')
                if q1 == 'no':
                    break
                else:
                    print('Our menu:')
                    print(self.menu)
                    pizza_name = input('Witch pizza?')
                    if pizza_name in self.menu.keys():
                        order.append(pizza_name)
                        cost = cost + int(self.menu[pizza_name])
                        print('Pizza added')
                        print(cost)
            return order, cost

pizzeria = Pizzeria()





if __name__ == "__main__":
    while True:
        q3 = input('continue?')
        if q3 == 'yes':
            role = input('choose role:')
            if role == 'admin':
                q2 = input('add or delete?')
                if q2 == 'add':
                    name_pizza = input('name pizza:')
                    price_pizza = int(input('price:'))
                    pizzeria.add_pizza(name_pizza, price_pizza)
                elif q2 == 'delete':
                    name_pizza = input('for deleting:')
                    pizzeria.remove_pizza(name_pizza)
            elif role == 'user':
                pizzeria.order_pizza()
            else:
                print('wrong')
        elif q3 == 'no':
            break
        else:
            print('mistake')


