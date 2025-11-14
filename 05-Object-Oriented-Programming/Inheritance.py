class Animal():

    def __init__(self):
        print('Animal created')

    def who_am_I(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Elephant(Animal):

    #re-writing base constructor is unnecessary,
    #do it only when we want to perform something extra
    def __init__(self):
        Animal.__init__(self)
        print('An elephant created')

    #Override
    def who_am_I(self):
        print('I am an elephant')

    def roar(self):
        print('Roaring...')

animal = Animal()   #Animal created
animal.eat()        #I am eating
animal.who_am_I()   #I am an animal

print('========================')
elephant = Elephant()   #Animal created
                        #An elephant created
elephant.eat()          #I am eating
elephant.who_am_I()     #I am an elephant
elephant.roar()         #Roaring...
