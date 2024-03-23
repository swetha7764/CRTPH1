class placements:
    def info(self,place):
        self.s=place
class dept(placements):
    def display(self,room):
        self.r=room
    def display(self):
        print(self.s,self.r,self.s)
p.placements("surampalem")
p.dept("f9")
p.display()
