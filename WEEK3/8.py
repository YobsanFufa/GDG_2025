class Animal:
    def make_sound(self):
        print("THIS is animal sound")
class Cat(Animal):
    pass
a1 = Animal()
a2=Cat()
print(a1.make_sound())
print(a2.make_sound())