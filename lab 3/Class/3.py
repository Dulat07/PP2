class Shape:
    def __init__(self):
        pass    
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)

qp = Shape()
qp.area()
length,width = map(int, input().split())
pq = Rectangle(length,width)
pq.area()

    

