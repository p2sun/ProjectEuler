from math import *

#using the Fibonacci approach does not give all
#pythagorean triplet
#it is a quick search for all triplets looking
#at the series of odd numbers (1,3,5,7,.....) taking advantage
#that the sum of n terms in that series is n**2

#let Term(i) be term i in the series
#let Sum(n) be sum of first n terms

#we know Sum(n)=n**2 and Sum(n-1)=(n-1)**2
#and Sum(n)=Sum(n-1)+Term(n) (equation 1)
#Sum(n) and Sum(n-1) are both perfect squares
#We just need to look for Term(n) that is also a perfect square
#to make equation 1 a sum of squares(or pythagorean form)
########e.g. c**2=n**2, b**2=(n-1)**2 and a=i**2 
#So we iterate through the odd series and check for perfect square
#terms and if a+b+c==1000

def pythagorean_triplet_odd(SumOfValues):
    x=int(SumOfValues/2)
    for i in xrange(0,x):
        term=(i*2)+1
        if(perfect_square(term)):
            sqrroot=term**0.5
            sumn=sqrroot+(i)+(i+1)
            if(sumn==SumOfValues):
                return sqrroot*(i+1)*i

#Dickson's Method Implementation
#can be found here http://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#Dickson.27s_method
#picked it because it was an easier implementation to understand compared to the general method
#this method guarantees all triplets to be found

def pythagorean_triplet_dickson(SumOfValues):
    end=int(floor(SumOfValues/3))+1
    for r in xrange(end,0,-2):
        y=(r**2)/2
        x=int(floor(y**0.5))
        for j in xrange(1,x):
            if y%j==0:
                s=j
                t=y/j
                sumn=3*r+2*(s+t)
                if(sumn==1000):
                    return s*r*t
            
            
def perfect_square(n):
    root=int(n**0.5)
    if(n==root**2):
        return True
    return False

print pythagorean_triplet_dickson(1000)
