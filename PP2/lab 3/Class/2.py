class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def getprint(self):
        print(self.length ** 2)

pq = Shape()
pq.area()
qp = Square(int(input()))
qp.getprint()
        