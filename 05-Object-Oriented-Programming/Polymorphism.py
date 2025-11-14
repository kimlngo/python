class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Must be implemented by subclass')
    
class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"
    
class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"
    

#never intended to create an abstract class nor call an abstract method
# animal = Animal('bob')
# animal.speak()

#create concrete class instead
niko = Dog('Niko')
print(niko.speak()) #Niko says woof!

print('=====================')
felix = Cat('Felix')
print(felix.speak()) #Felix says meow!

print('=====================')
animal_list = [niko, felix]
for animal in animal_list:
    print(animal.speak())

#Niko says woof!
#Felix says meow!