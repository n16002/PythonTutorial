from . level2 import Animate


class Animals(Animate):
    def breathe(self):
        pass

    def move(self):
        pass

    def eat_food(self):
        pass


class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')


class Giraffes(Mammals):
    print('eating leaves')


class Cat(Mammals):
    pass


class Human(Mammals):
    def __init__(self, name):
        self.name = name

    def self_introduction(self):
        print("Hi, I'm", self.name, '.')