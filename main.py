'''from dog import Dog
from bird import Bird
a = Dog(10)
a.sleep(3)
a.run()
a.dogMakeSond()
b = Bird(90)
b.flyB()
b.BirdMakeSound()
b.move()'''

from factory import Fact
from singlton import SingletonClass

r = Fact(15)
x = r.getObsect()
x.drink()


ob = SingletonClass()
print(ob)

ob2 = SingletonClass()
print(ob2)





