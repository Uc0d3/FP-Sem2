from functions import *
from tests import run_tests

options = """
1 - Add pizza
2 - Filter by name
3 - Filter by price greater than
Option:
"""


pizzas = []

run_tests()

while True:
    print(pizzas)
    try:
        op = int(input(options))
        if op == 1:
            pizza = make_pizza(pizzas)
            add_pizza(pizzas, pizza)
        if op == 2:
            name = input("Name:")
            filtered_pizzas = filter_by_name(pizzas, name)
            print_pizzas(filtered_pizzas)
        if op == 3:
            price = int(input("Price:"))
            filtered_pizzas = filter_by_price(pizzas, price)
            print_pizzas(filtered_pizzas)
    except Exception as e:
        print(e)
