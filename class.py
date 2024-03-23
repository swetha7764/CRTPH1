class f15:
    def light(self):
        print("ok switching on the lights")
    def fan(self,speed):
        print("fan is on and the speed is",speed)
        self.s=speed
    def cpu(self):
        print("powering on the system")
        print(self.s)
chandu =f15()
chandu.light()
chandu.fan(5)
chandu.cpu()
 

class shopping:
    def dresstype(self,dresstype):
        print("type of the dress",type)
        self.s=dresstype
    def price(self,price):
        print("price of the dress",price)
        self.t=price
    def size(self,size):
        print("size of the user",size)
        self.p=size
    def display(self,display):
        print(self.s,self.t,self.p)
swetha=shopping()
swetha.dresstype("kurta")
swetha.price(600)
swetha.size("m")
swetha.display()
