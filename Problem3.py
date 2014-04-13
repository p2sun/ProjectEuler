#The approach I had was to go through starting from 2 and find
#and keep track of the prime numbers and keep track of the prime
#factors of n.

#first check if current number is prime by iterating through the list of
#primes less than current and seeing if divisible
#if not and it can divide n evenly then add it to list of prime factor
#and reduce n by that factor

#return last known prime factor or last element in primeFactor list

def largest_prime_factor(n):
    primes=[]
    primeFactor=[]
    i=2
    while (i<=n):
        if (len(primes)==0):
            primes.append(i)
            if(n%i==0):
                primeFactor.append(i)
                n=n/i
        else:
            prime=True
            for j in primes:
                if j>=i or i%j==0:
                    prime=False
                    break
            if prime:
                primes.append(i)
                if (n%i == 0):
                    primeFactor.append(i)
                    n=n/i
        i+=1
    return primeFactor[-1]
print largest_prime_factor(600851475143)
