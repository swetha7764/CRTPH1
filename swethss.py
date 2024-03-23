lass carshowroom:
    def company(self,name):
        l=["toyato","TATA","suziki"]
        if name in l:
            print("welcome to the family of ",name)
    def model(self,name):
        d={"toyato":["fortunate","innova"],"TATA":["nexon","tiger"],"suziki":["swift","alto"]}
        if name in d:
            print(d[name])
    def price(self,m):
        price_list={"fortune":750000,"innova":800000,"nexon":1200000,"tiger":1100000,"swift":500000,"alto":400000}
        print("the model of the car",m)
        showroom_price=price_list[m]
        print("price of the car",showroom_price)
        if m in price_list:
            cgst=0.18
            gst1=cgst*2
            sgst=0.18
            gst2=sgst/2
            gst=(gst1+gst2)*showroom_price
            insurance=100000
            final_price=showroom_price+gst+insurance
            print("final price of the car",final_price)
n=input("enter the company of the car")
n=input("enter the model of the car")
a=carshowroom()
a.company(n)
a.model(n)
a.price(m)
print(a)

