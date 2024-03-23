class shopping:
    def __init__(self,place):
        self.place=place
        print("welcoming to shopping at",place)
    def dresstype(self,type):
        self.t=type
    def price(self,price):
        self.p=price
    def size(self,size):
        self.s=size
    def display(self):
        print(self.place,self.t,self.p,self.s)
k=shopping("kalamandir")
k.dresstype("kurta")
k.price(600)
k.size("L")
k.display()
