#Problem: Find lowest common multiple of numbers from 1 to 20

#Runtime is less than O(n*lgn) 
#Applied Sieve inspired approach

#Goal is to reduce each element in the list to a prime
#number or 0

#Iterate through a list of integers from 1 to 20
#If the current element is not 0 then it is a prime factor
#we multiply that prime into our product variable counter
#We then iterate through the list by that prime factor to reduce
#all elements past that element which is a multiple of that factor


product=1
factors=range(1,21)
for i in range(1,20):
    composite=factors[i]
    if(composite!=0):
        product*=composite
        for j in range(i+composite,20,composite):
            factors[j]/=composite
print product
