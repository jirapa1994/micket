from turtle import *
#bobobobobobbiuhihodphbkerperkgpk orkew  final leaw na ja
class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n*1.5, 2) 
        self.fillcolor(n/6., 0, 1-n/6.)
        self.st()
class Tower(list,Turtle):
    def __init__(self, x):
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d


def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)


 
   

def main():
    global t1, t2, t3
    ht(); penup(); goto(0, -225)  
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    t = Turtle()
    t.st()
    t.pu()
    t.goto(-260,-150)
    t.pd()
    t.fd(20)
    t.left(90)
    t.fd(300)
    t.left(90)
    t.fd(20)
    t.left(90)
    t.fd(300)
    t.left(90)

    t.pu()
    t.goto(-10,-150)
    t.pd()
    t.fd(20)
    t.left(90)
    t.fd(300)
    t.left(90)
    t.fd(20)
    t.left(90)
    t.fd(300)
    t.left(90)

    t.pu()
    t.goto(240,-150)
    t.pd()
    t.fd(20)
    t.left(90)
    t.fd(300)
    t.left(90)
    t.fd(20)
    t.left(90)
    t.fd(300)
    t.left(90)
    for i in range(3,0,-1):
        t1.push(Disc(i))
    
    hanoi(3, t1, t2, t3)
    return "EVENTLOOP"

if __name__=="__main__":
    
    msg = main()
    mainloop()
