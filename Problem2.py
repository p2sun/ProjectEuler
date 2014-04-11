#Fastest way to go through a fibonacci
#sequence is in O(n) through iteration

#iterate through the sequence until the
#leading term a2 exceeds 4 million

def even_fibonacci(n):
    a1=a2=1
    sum=0
    tmp=0
    while(a2<=n):
        tmp=a2
        a2+=a1
        a1=tmp
        if(!(a2%2)):
            sum+=a2
    return sum

print even_fibonacci(4000000)     
        
            
        
