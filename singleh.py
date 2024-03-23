class shopping:
    def __init__(self,place):
        self.place=place
        print("welcome to shopping",place)
    def dresstype(self,type):
        self.t=type
    def price(self,price):
        self.p=price
    def size(self,size):
        self.s=size
    def display():
        print(self.place,self.t,self.p,self.s)
k=shopping("CMR")
k.dresstype("jeans")
k.price(900)
k.size("L")
k.display()
