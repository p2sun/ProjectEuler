#Problem: Find the 10 001st prime number?
def prime(n):
    n-=1
    primes=[2]
    current=1
    while(n>0):
        current+=1
        if(is_prime(current,primes)):
            primes.append(current)
            n-=1
    return primes[-1]

def is_prime(n,primes):
    for i in primes:
        if(n%i==0):
            return False
    return True

print prime(10001)
