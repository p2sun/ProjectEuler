#Problem: The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#The approach I had was to go through starting from 2 and find
#and keep track of the prime numbers and keep track of the prime
#factors of n.

#first check if current number is prime by iterating through the list of
#primes less than current and seeing if divisible
#if not and it can divide n evenly then add it to list of prime factor
#and reduce n by that factor

#return last known prime factor or last element in primeFactor list

def largest_prime_factor(n):
    i=2
    
    while (i<=n):
        if (n%i == 0):
            n=n/i
        i+=1
    return i-1
print largest_prime_factor(600851475143)
