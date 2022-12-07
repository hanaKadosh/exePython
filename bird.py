from animals import Animals


class Bird(Animals):
    def __init__(self, mk):
        super().__init__()
        self.mk = mk

    def flyB(self):
        print("my kilomatar :", self.mk)

    def BirdMakeSound(self):
        super().makeSound('z z z')

    def move(self):
        print('bird move')