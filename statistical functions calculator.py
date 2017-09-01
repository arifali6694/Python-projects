import time
t = time.time()
e = (1 + (float(1) / 10000000000)) ** 10000000000

def fact(n):
    i = 2
    s = 1
    while i <= n:
        s *= i
        i += 1
    return s

def ncr(n, r): #returns the facorial of the input. 
    return fact(n) / (fact(r) * fact(n-r))


class Sample():  # creating a random sample from an observation

    def __init__(self, list):
        self.list = list

    def sum(self):
        s = 0
        for i in self.list:
            s += i
        return s

    def mean(self):
        s = self.sum()
        return float(s) / len(self.list)

    def var(self):
        m = self.mean()
        s = 0
        for i in self.list:
            s += float((i - m) ** 2) / (len(self.list) - 1)
        return s

    def stddev(self):
        s = self.var()
        return s ** 0.5


class Binomial():

    def __init__(self, n, p):
        self.n = float(n)
        self.p = float(p)


    def mean(self):
        return self.n * self.p

    def var(self):
        return self.n * self.p * (1 - self.p)

    def stddev(self):
        s = self.var()
        return s ** 0.5

    def probx(self, x): #probability distribution of x
        return ncr(self.n, x) * (self.p ** x) * ((1 - self.p) ** (self.n - x))

    def cumprobx(self, x):  #Works out the cumulative probability of x
        s = 0
        i = 0
        while i <= x:
            s += self.probx(i)
            i += 1
        return s

    def invcumprobx(self, x):  #Works out the chance of x or more trials being successful
        return 1 - self.cumprobx(x) + self.probx(x)


class Poisson(): # pdf function for the poisson distribution

    def __init__(self, p):
        self.p = p

    def mean(self):
        return "It's the parameter %.2f " % self.p

    def var(self):
        return "It's the parameter %.2f " % self.p
    
    def stddev(self):
        return self.p ** 0.5

    def probx(self, x): #probability distribution of x
        return ((self.p ** x) * (e ** (-1 * self.p))) / fact(x)
    
    def cumprobx(self, x):  #Works out the chance of x or less trials being successful.
        s = 0
        i = 0
        while i <= x:
            s += self.probx(i)
            i += 1
        return s

    def invcumprobx(self, x):  #Works out the chance of x or more trials being successful.
        return 1 - self.cumprobx(x) + self.probx(x)

sample1 = Poisson(0.6)
print sample1.mean()
print sample1.cumprobx(50)

ylist = [0, 1, 2, 2, 2, 3]
q = Sample(ylist)
print q.sum()


t = time.time() - t
#print "This took %.3f seconds" % (t)        


#geometric function , pdf and cdf calc


class Geo():
    
    def __init__(self , p): # p = sucess rate
         self.p = float(p)

    def pdf (self , x): # pdf fucntion(x= trials)
	self.x = float(x)
        return self.p * (1- self.p)** (x - 1) , self.x

    def mean (self):
        return 1 / pdf(x)
       
        
t1 = Geo(0.5)
print t1.pdf(10) ,

  
