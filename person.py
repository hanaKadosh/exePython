class Person(object):
    def __new__(cls, *args, **kwargs):
        print('new')
        return object.__new__(cls)

    def __init__(self):
        print('init')
        self.instanceM()

    def instanceM(self):
        pass
