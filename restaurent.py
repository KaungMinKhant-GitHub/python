


class restaurent:
    
    menu = {
        'puzza' : 4000 ,
        'coffee' : 1000 ,
        'water' : 200 ,
        'cake' : 2500
    }
    def __init__(self) : 
        self.total_bill = 0
        self.orders = []

    def addorder(self , order) :
        self.orders.append(order)
        self.total_bill+= self.menu[order]

    def print_bill(self) : 
        for order in self.orders:
            print(f"{order} : {self.menu[order]}")

        print(f"Total Bill is {self.total_bill}")

    

def start() : 
    table = restaurent()
    
    while True:
        order = input('Order : ')
        table.addorder(order)
        another = input("Wana order y/n : ")
        if another == 'y':
            continue
        else:
            table.print_bill()
            break

start()

  