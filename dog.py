from animals import Animals


class Dog(Animals):
    def __init__(self, km):
        super().__init__()
        self.km = km

    def run(self):
        print('dog run km:'+str(self.km))

    def dogMakeSond(self):
        super().makeSound('hav hav')

    def move(self):
        print('dog move')