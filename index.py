person = {}

while True:
    name = input('Enter Your name : ')
    age = input('Enter Your age : ')
    person[name] = age

    b= input('You wana break y/n :')

    if b == 'y':
        continue
    else:
        break

for keys,values in person.items():
    print(f'{keys} is {values} years old.')


