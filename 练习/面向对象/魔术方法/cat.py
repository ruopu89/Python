import animal
from animal import Animal

class Cat(Animal):
    x = 'cat'
    y = 'abcd'

class Dog(Animal):
    def __dir__(self):
        return ['dog']

print('-----------------------------------')
print('Current Module\'s name = {}'.format(dir()))
print('animal Module\'s names = {}'.format(dir(animal)))
print("object's __dict__ = {}".format(sorted(object.__dict__.keys())))
print("Animal's dir() = {}".format(dir(Animal)))
print("Cat's dir() = {}".format(dir(Cat)))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
tom = Cat('tome')
print(sorted(dir(tom)))
print(sorted(tom.__dir__()))
print(sorted(set(tom.__dict__.keys()) | set(Cat.__dict__.keys()) | set(object.__dict__.keys())))
print("Dog's dir = {}".format(dir(Dog)))
dog = Dog('snoppy')
print(dir(dog))
print(dog.__dict__)