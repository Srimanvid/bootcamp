# inheritance
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print('dog is barking')
    def sleep(self):
        print('dog is sleeping')    

class puppy(dog):
    def play(self):
        print('dog is playing')
a=puppy()
        