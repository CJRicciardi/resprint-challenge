# sprint-challenge-3.1 / acme_report.py

from acme import Product
from random import randint, uniform

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']

NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num=30):
    product_list = []
    first = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    second = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
    for n in list(range(num)):
        x = randint(0, 4)
        y = randint(0, 4)
        name = f'{first[x]} {second[y]}'
        # print(name)
        price = randint(5, 101)
        weight = randint(5, 101)
        flammability = uniform(0, 2.5)
        # print(flammability)
        product_list.append(Product(name=name, price=price, weight=weight, flammability=flammability))
    return product_list

# product_list = generate_products()

def inventory_report(products):
    prod = []
    price = []
    for i in list(range(len(products))):
        prod.append(products[i].name)
        price.append(products[i].price)
    n = len(set(prod))
    mean = sum(price) / len(price)
    return print(f'The list of products has {n} unique items, and an average price of {mean: .2f}.')

# inventory_report(product_list)

# print(list(range(len(product_list))))