"""
Ball rolling down a rough slope example :
We will use a class for the forces acting on the ball and for the motion of the
ball on the slope.
To create a new ball (object) we will pass an instance through the
Slope() clas which will
also inherit attrbutes of the class.
The variables ’ u,v,a,s,t,inc,c,m ‘ represent initial conditions for
the ball - will be explained below.
"""
import math
g = 9.81  # acceleration due to gravity.
pi = math.pi


class Slope():  # variables of forces present in the plane
    def __init__(self, list1):
        self.inc = float(list1[5])
        self.m = float(list1[7])
        self.wt = self.m*g*math.sin(pi/180*float(list1[5]))  
        # forces acting along the slope.
        self.re = self.m*g*math.cos(pi/180*float(list1[5]))  
        # forces acting along perpendicular to the slope.
        self.c = float(list1[6])
        self.u = float(list1[0])
        self.v = float(list1[1])
        self.s = float(list1[3])
        self.t = float(list1[4])
        self.a = float((self.wt - (self.c*self.re))/self.m)

    def resolve(self):  # (wt-(c*re))/m=a
        self.a = float((self.wt - (self.c*self.re))/self.m)
        return self.a
        
    def finalspeed(self):
        self.v = self.u + (self.a * self.t)
        return self.v 
        
    def initialspeed(self):
        self.u = self.v - (self.a * self.t)
        return self.u 
    
""" create a list with the following initial conditions respectively sepreated 
by commas, if unknown put 0. 
u(initial velocity ),
v(final velocity),
a (acceleration)
s (legnth of slope)
t (time taken to travel on slope)
inc (angle of inlcine of slope,between 0 - 90 degrees)
c (friction coefficient)
m (mass)   

""" 
# example 1: we have some of the inital conditions to find the final velocity.
list1 = [0, 0, 0, 10, 10, 45, 0, 10] 
b1 = Slope(list1)  # create a ball (instance) to pass through class. 
print ('finalspeed of ball 1=', b1.finalspeed()) 

# example 2:we have some of the inital conditions to find the initial velocity.
list2 = [0, 100, 0, 10, 10, 45, 0, 10] 
b2 = Slope(list2)
print ('initialspeed of ball 2=', b2.initialspeed())

# example 3: we have some conditions to find the acceleration of the ball.
list3 = [0, 100, 0, 10, 10, 60, 0, 10] 
b3 = Slope(list3)
print ('acceleration of ball 3 = ', b3.resolve()) 