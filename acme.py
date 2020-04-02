# Sprint-challenge-3.1/Product.py

from random import randint

class Product:
    '''
    This class is to keep track of all of acme corporations products.
    Varaibles:
    name - string (no default)
    price - integer (default 10)
    weight - integer (default 20)
    flammability - float (default 0.5)
    identifier - integer (default randomly generated uniform number between 1000000 & 9999999)
    '''
    def __init__(self, name=None, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 10000000)

    def stealability(self):
        steal_ratio = self.price / self.weight
        if steal_ratio < 0.5:
            return 'Not so stealable...'
        elif steal_ratio >= 0.5 and steal_ratio < 1.0:
            return 'Kinda Stealable...'
        else:
            return 'Very stealable!'

    def explode(self):
        boom_ratio = self.flammability * self.weight
        if type(self).__name__ == 'BoxingGlove':
            return "...it's a glove."
        else:
            if boom_ratio < 10:
                return '...fizzle'
            elif boom_ratio >= 10 and boom_ratio < 50:
                return '...boom!'
            else:
                return '...BABOOM!!'

class BoxingGlove(Product):
    def __init__(self, name=None, price=10, weight=10,flammability=0.5):
        super().__init__(name=name, price=price, weight=weight,flammability=flammability, )

    def punch(self):
            if self.weight < 5:
                return 'That tickles.'
            elif self.weight >= 5 and self.weight < 15:
                return 'Hey that hurt!'
            else:
                return 'OUCH!'























    # @auto_attr_check
    # class Product(object):
    #     name = str
    #     price = int
    #     weight = int
    #     flammability = float
    # why the f* are they asking us to be precise with field types, when they are checking it?  I spent a couple hours trying to figure that out!!  (No wonder I figured there is no way i could pass the challenge originally). I'm curious to be able to do it, but I don't have that kind of time during a test!
