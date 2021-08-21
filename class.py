class Person : 
    def __init__(self,name , age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"{self.name} is {self.age}")

p = Person('aunguan',20)
p.info()