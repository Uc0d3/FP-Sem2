from functions import add_pizza, filter_by_name, filter_by_price


def add_pizza_test():
    pizza1 = {
        "id": 1,
        "name": "Margherita",
        "price": 20
    }
    pizza2 = {
        "id": 2,
        "name": "Vegana",
        "price": 25
    }
    pizza3 = {
        "id": 3,
        "name": "Kanibale",
        "price": 30
    }
    pizzas_test = []
    add_pizza(pizzas_test, pizza1)
    assert pizzas_test == [pizza1]

    add_pizza(pizzas_test, pizza2)
    assert pizzas_test == [pizza1, pizza2]

    add_pizza(pizzas_test, pizza3)
    assert pizzas_test == [pizza1, pizza2, pizza3]

    print("Add pizza test passed")


def filter_pizzas_by_name_test():
    pizza1 = {
        "id": 1,
        "name": "Margherita",
        "price": 20
    }
    pizza2 = {
        "id": 2,
        "name": "Vegana",
        "price": 25
    }
    pizza3 = {
        "id": 3,
        "name": "Kanibale",
        "price": 30
    }
    pizzas_test = []
    add_pizza(pizzas_test, pizza1)
    add_pizza(pizzas_test, pizza2)
    add_pizza(pizzas_test, pizza3)

    filtered = filter_by_name(pizzas_test, "Veg")
    assert filtered == [pizza2]

    print("Filter by name test passed")


def filter_pizzas_by_price_test():
    pizza1 = {
        "id": 1,
        "name": "Margherita",
        "price": 20
    }
    pizza2 = {
        "id": 2,
        "name": "Vegana",
        "price": 25
    }
    pizza3 = {
        "id": 3,
        "name": "Kanibale",
        "price": 30
    }
    pizzas_test = []
    add_pizza(pizzas_test, pizza1)
    add_pizza(pizzas_test, pizza2)
    add_pizza(pizzas_test, pizza3)

    filtered = filter_by_price(pizzas_test, 20)
    assert filtered == [pizza2, pizza3]

    print("Filter by price test passed")

def run_tests():
    add_pizza_test()
    filter_pizzas_by_name_test()
    filter_pizzas_by_price_test()
