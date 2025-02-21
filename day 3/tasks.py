class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print('dog is barking')

    def sleep(self):
        print('dog is sleeping')


dog1=dog('vamshi',8)
dog1.bark()
dog1.sleep()
print(dog1.name)
#2task
class dog_1:
    def __init__(self,name,age):
        self.name,self.age=name,age
tommy=dog_1('mohan',8)
print(tommy.name,tommy.age) 
#3 task
class puppy(dog):
    pass
sr=puppy('jake',5)
print(sr.bark())



    

 

