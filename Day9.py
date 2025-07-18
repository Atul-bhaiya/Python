# Polymorphism

class Bird :
    def sound(self):
        print("Bird sounds ")

class Parrot(Bird):
    def sound(self):
        print("Parrot says: Mitthu Mitthu")


class Cow(Bird):
    def sound(self):
        print("Crow says: Caw Caw")


for Bird in (Parrot() , Cow()):
    Bird.sound()




