def make_pizza(pizzas):
    id = len(pizzas) + 1
    nume = input("Name:")
    price = int(input("Price:"))
    pizza = {
        "id": id,
        "name": nume,
        "price": price
     }
    return pizza


def filter_by_name(pizzas, name):
    filtered = [pizza for pizza in pizzas if name in pizza["name"]]
    return filtered


def filter_by_price(pizzas, price):
    filtered = [pizza for pizza in pizzas if pizza["price"] > price]
    return filtered


def print_pizzas(pizzas):
    print("Pizzas:")
    for pizza in pizzas:
        print ("Name: %s Price: %d" % (pizza["name"], pizza["price"]))


def add_pizza(pizzas, pizza):
    pizzas.append(pizza)
