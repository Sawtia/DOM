import json



class Pizzeria:

    def __init__(self, menu):
        self.menu = menu

    def load_menu(self):
        with open('menu.json', 'r') as f:
            json.load(f)
            return json.load(f)

    def save_menu(self):
        with open('menu.json', 'w') as f:
            return json.dump(menu, f)

    def add_pizza(self, price):
        Pizzeria.load_menu(self)
        if self in menu.keys():
            print('already there is')
        else:
            menu[self] = price
        return Pizzeria.save_menu(menu)

    def remove_pizza(self):
        Pizzeria.load_menu(self)
        if self in menu.keys():
            print('delete')
            del menu[self]
        else:
            print('no pizza')
        return Pizzeria.save_menu(menu)

    def order_pizza(self):
        Pizzeria.load_menu(self)
        order = []
        cost = 0
        while True:
            q1 = input('continue?')
            if q1 == 'no':
                break
            else:
                print('Our menu:')
                print(menu)
                pizza_name = input('Witch pizza?')
                if pizza_name in menu.keys():
                    order.append(pizza_name)
                    cost = cost + int(menu[pizza_name])
                    print('Pizza added')
                    print(cost)
        return (order, cost)




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
                    Pizzeria.add_pizza(name_pizza, price_pizza)
                elif q2 == 'delete':
                    name_pizza = input('for deleting:')
                    Pizzeria.remove_pizza(name_pizza)
            elif role == 'user':
                Pizzeria.order_pizza(1)
            else:
                print('wrong')
        elif q3 == 'no':
            break
        else:
            print('mistake')
