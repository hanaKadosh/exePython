class Cocacola(object):
    def drink(self):
        print('drink cola')


class Sprite(object):
    def drink(self):
        print('drink cola')


class Fact(object):
    def __init__(self, x):
        self.x = x

    def getObsect(self):
        if self.x > 10:
            return Cocacola()
        else:
            return Sprite()
