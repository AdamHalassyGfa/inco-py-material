
class animal:
    def __init__(self, color):
        self.color = color
        print(f"An {self.color} animal is born.")

    def walk(self):
        print(f"The {self.color} animal is walking.")


redAnimal = animal("red")
redAnimal.walk()

blueAnimal = animal("blue")
blueAnimal.walk()

zoo = [redAnimal, blueAnimal]
for animal in zoo:
    animal.walk()