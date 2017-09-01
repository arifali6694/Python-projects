"""
Ball rolling down a rough slope example :
We will use a class for the forces acting on the ball, a class for the motion of the ball on the slope.
To create a new ball  we will pass a new variable through the ball class which will
also inherit the slope class.
The variables ’ u,v,a,s,t,inc,c,m ‘ represent initial conditions for the ball on the slope will be used to calculate the outputs which.

"""
import math 
g=9.81
pi = math.pi

str1=(raw_input('Enter u,v,a,s,t,inc,c,m respectively with spaces instead of commas ,if unknown put 0.'))
print str1 
list1 = str1.split()
list1 = [float(e) for e in list1]
print [i for i in list1]

class Slope(): # variables on forces present in the plane
    def __init__(self ,list1):
        self.inc = float(list1[5])
        self.m= float(list1[8])
        self.wt = self.m*g*math.sin(pi/180*float(list1[5]))
        self.re = self.m*g*math.cos(pi/180*float(list1[5]))
        self.c = float(list1[6])
        self.u = float(list1[0])
        self.v = float(list1[1])
        self.s = float(list1[3])
        self.t = float(list1[4])
        print self.u ,self.v

    def resolve(self): #wt-(c*re)=m*a
        self.a = float((self.wt - (self.c*self.re))/self.m)
        return self.a
    
    def finalspeed(self):
         self.v = self.u + (self.a*self.t)
         return self.v , self.u
        
    def initialspeed(self):
        self.u = self.v - (self.a* self.t)
        return self.u ,self.v
    
list1 = [1,2,3,4,5,6,7,8,9,10,11]
list1= [raw_input('Enter u,v,a,s,t,inc,c,m respectively:')] # creating arbitrary conditions for ball on the slope 
print list1 
b2 = Slope(list1) # create an object to pass through class . 

print 'acc = ', b1.resolve() #calculates acceleration based on given initial conditions
print 'initialspeed=', b1.initialspeed() #calculates initial speed based on given initial conditions
print 'finalspeed=', b1.finalspeed() #calculates final speed based on given initial conditions

                


