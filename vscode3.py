":
      ato      while True:
                print("select from fortuner and Lc")
                self.choice=input("enter the car company")
                if self.choice=="fortuner":
                   self.price(self.choice)
                   break
                elif self.choice==Lc:
                     self.choice(self.choice)
                     break
                else:
                    print("invalid")
        elif self.n="mahindra":
            while True:
                 print("select from thar and tech")
                 self.choice=input("enter the car company")
                 if self.choice=="thar":
                    self.price(self.choice)
                    break 
                 elif self.choice=="tech":
                      self.price(self.choice)
                      break
                 else:
                     print("invalid")
    def price(self.choice):
        if choice=="alto":
            self.p=400000
        elif choice=="fortuner":
            self.p=1000000
        elif choice=="thar":
            self.p=1200000
        else:
            print("enter valid")
        total_p=self.p+self.cgst+self.sgst+self.insurance
        print(total_p)
c=car()
c.company()










class car:
    def __init__(self):
        cgst=0.18
        sgst=0.19
        insurance=100000
    def company(self):
        while True:
              print("suziki,toyato,mahindra")
              self.n=input("enter the car company")
              if self.n=suziki:
                 print("welcome to suziki")
                 self.model()
                 break
              elif self.n=toyato:
                   print("welcome to toyato")
                   self.model()
                   break
              elif self.n=mahindra:
                   print("welcome to mahindra")
                   self.model()
                break
              else:
                 print("enter valid company")
    def model(self): 
        if self.n="suziki":
            while True:
                print("select from swift and alto")
                self.choice=input("enter the car company")
                if self.choice=="swift":
                    self.price(self.choice)
                    break
                elif self.choice=="alto":
                    self.price(self.choice)
                    break
                else:
                    print("enter valid")
        elif self.n="toyoto":
             while True:
                print("select from fortuner and Lc")
                self.choice=input("enter the car company")
                if self.choice=="fortuner":
                   self.price(self.choice)
                   break
                elif self.choice==Lc:
                     self.choice(self.choice)
                     break
                else:
                    print("invalid")
        elif self.n="mahindra":
            while True:
                 print("select from thar and tech")
                 self.choice=input("enter the car company")
                 if self.choice=="thar":
                    self.price(self.choice)
                    break 
                 elif self.choice=="tech":
                      self.price(self.choice)
                      break
                 else:
                     print("invalid")
    def price(self.choice):
        if choice=="alto":
            self.p=400000
        elif choice=="fortuner":
            self.p=1000000
        elif choice=="thar":
            self.p=1200000
        else:
            print("enter valid")
        total_p=self.p+self.cgst+self.sgst+self.insurance
        print(total_p)
c=car()
c.company()