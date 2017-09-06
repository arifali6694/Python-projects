"""
import time
t = time.time()
e = (1 + (float(1) / 10000000000)) ** 10000 # eulers number
"""


def fact(n):    # factorial function.
    i = 2
    s = 1
    while i <= n:
        s *= i
        i += 1
    return s


def ncr(n, r): 
    return fact(n) / (fact(r) * fact(n-r))


class Sample():  # class for a random sample .

    def __init__(self, list):  # list contains he values of the random sample.
        self.list = list

    def sum(self):
        s = 0
        for i in self.list:
            s += i
        return s

    def mean(self):  # wokring out the mean of the random sample.
        s = self.sum()
        return float(s) / len(self.list)

    def var(self):  # wokring out the variance of the random sample.
        m = self.mean()
        s = 0
        for i in self.list:
            s += float((i - m) ** 2) / (len(self.list) - 1)
        return s

    def stddev(self):  # wokring out standard deviation of the random sample.
        s = self.var()
        return s ** 0.5


class Binomial():  # class for a binomially distributed random variable x.

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

    def probx(self, x):  # probability distribution function of x.
        return ncr(self.n, x) * (self.p ** x) * ((1 - self.p) ** (self.n - x))

    def cumprobx(self, x):  # cumulative distribution function of x.
        s = 0
        i = 0
        while i <= x:
            s += self.probx(i)
            i += 1
        return s

    def invcumprobx(self, x):  # inverse cumulative distribution function of x.
        # Works out the chance of  being successful in x trials or more.
        return 1 - self.cumprobx(x) + self.probx(x)


class Poisson():  # class for a poisson distributed random variable x

    def __init__(self, p):
        self.p = p

    def mean(self):
        return self.p

    def var(self):
        return self.p
    
    def stddev(self):
        return self.p ** 0.5

    def probx(self, x):  # probability distribution function of x.
        return ((self.p ** x) * (e ** (-1 * self.p))) / fact(x)
    
    def cumprobx(self, x):  # cumulative distribution function of x.
        # Works out the chance of being successful in trials x or less.
        s = 0
        i = 0
        while i <= x:
            s += self.probx(i)
            i += 1
        return s

    def invcumprobx(self, x):  
            # Works out the chance of  being successful in x trials or more.
            return 1 - self.cumprobx(x) + self.probx(x)
# examples
sample1 = Poisson(0.6)
print sample1.mean()
print sample1.cumprobx(50)

ylist = [0, 1, 2, 2, 2, 3]
q = Sample(ylist)
print q.sum()

# geometric function , pdf and cdf calc


class Geo():  # class for a geometrically distributed random variable x.
    
    def __init__(self, p):  # p = sucess rate
        self.p = float(p)

    def pdf(self, x):  # # probability distribution function of x, (x = trials)
        self.x = float(x)
        return self.p * (1 - self.p) ** (x - 1), self.x

    def mean(self):
        return 1 / pdf(x)
       
        
t1 = Geo(0.5)
print t1.pdf(10),
