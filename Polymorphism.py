class Cat:
    def __init__(self):
        pass
    def makesound(self):
        return f'I can Meow!'


class Dog:
    def __init__(self):
        pass
    def makesound(self):
        return f'I can bark!'

    #Function for polymorphism
    def animal_sound(animal):
        animal.makesound()

#class instances
cat = Cat()
dog = Dog()

print(cat.makesound())
print(dog.makesound())