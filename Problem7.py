#Problem: Find the 10 001st prime number?
def prime(n):
    n-=1
    primes=[]
    current=2
    while(n>0):
        current+=1
        if(perfect_square(current)== False):
            if(is_prime(current,primes)):
                primes.append(current)
                n-=1
    return primes[n-2]

def is_prime(n,primes):
    if(n%2==0):
        return False
        
    if(primes==[]):
        return True
        
    for i in primes:
        if(n%i==0):
            return False
    return True

def perfect_square(n):
    root=int(n**0.5)
    if(n==root**2):
        return True
    return False

print prime(10001)
