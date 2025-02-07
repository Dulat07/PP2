class Point:
    def __init__(self,x,y):
       self.x = x 
       self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self,new_x,new_y):
        self.x = new_x
        self.y = new_y
    def dist(self,other_point):
        return ((self.x - other_point.x)** 2 + (self.y - other_point.y)** 2) ** 0.5

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())

p1 = Point(x1,y1)
p2 = Point(x2,y2)

p1.show()
p2.show()

new_x,new_y = map(int,input().split())
p1.move(new_x,new_y)
p1.show()

distance = p1.dist(p2)
print(f"Answer is : {distance:.2f}")
