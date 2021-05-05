class Animal:
    __foot_count = 4
    name = 'NO NAME'

    def voice(self):
        print('not typed can not something say')


class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def voice(self):
        print(self.name, 'GAV-GAV')


class Cat(Dog):

    def __init__(self, name):
        self.name = name

    # override or overload
    def voice(self):
        super(Cat, self).voice()
        print(self.name, 'MEOW-MEOW')


c = Cat('Kisa')
c.voice()
