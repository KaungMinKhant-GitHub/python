class person:
    def __init__(self,name , age):
        self.name = name 
        self.age = age  

    def greet(Print_func):
        def hello(a):
            print('this is hello start!')
            Print_func(a)
            print('this is the end.')
        return hello
    @greet
    def print(self):
        print(f'{self.name} is {self.age}')

class animal:
    def __init__(self):
        self.name = 'dog'

    def d_sound(self):
        print(f'{self.name}ho ho')

class attribute(animal):
    def __init__(self):
        super().__init__()
    

        
a =attribute()
a.d_sound()

x = person('kaungminkhant' , 21)
x.print()