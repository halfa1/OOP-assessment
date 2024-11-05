class Animal:
    def __init__(self):
       return None
    def eat(self,name):
        return f'{name}i can eat'
    def sleep(self,name):
        return f'{name}, i can sleep'

class Dog(Animal):
    def bark(self,name):
        self.name = name
        return f'{name},i can bark'

dog1= Animal()

print(dog1.sleep('john'))

dog2= Dog()
print(dog2.sleep('john2'))