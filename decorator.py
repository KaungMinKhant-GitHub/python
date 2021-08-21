

def greet(normal_fun):
    def wrapper(name):
        #before
        print('i am before ')
        normal_fun(name)
        #after
        print('i am after')
    return wrapper

@greet
def myfun(name):
    print(f'{name} is funname')
myfun('kaungminkahnt')