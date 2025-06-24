class Mammal():
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("{} is eating".format(self.name))
    def greet(self):
        print("{} is greeting".format(self.name))
class Human(Mammal):
    def __init__(self,name,hand):
        super().__init__(name)
        self.hand=hand
    def wave(self):
        print("With shacking {} hand".format(self.hand))
    def walk(self):
        print("{} is walking".format(self.name))
    def greet(self):
        self.wave()
        super().greet()
class speed(Human):
    def __init__(self,name,hand):
        super().__init__(name,hand)
    def walking(self):
        print("{} fast".format(super.walk()))

person=Human("Kim", "right")
person.greet()
person.walk()
person.eat()


    