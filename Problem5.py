#
product=1
factors=range(1,21)
for i in range(1,20):
    composite=factors[i]
    if(composite!=0):
        product*=composite
        for j in range(i+composite,20,composite):
            factors[j]/=composite
print product
