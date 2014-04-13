#Problem: The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#The approach I had was to go through starting from 2 and find
#and if n is divisible by current number(i), reduce it. i is a prime
#because if it were composite, it wouldn't be able to divide n
#since n has already been reduce by its prime factors less than itself


def largest_prime_factor(n):
    i=2
    
    while (i<=n):
        if (n%i == 0):
            n=n/i
        i+=1
    return i-1
print largest_prime_factor(600851475143)
