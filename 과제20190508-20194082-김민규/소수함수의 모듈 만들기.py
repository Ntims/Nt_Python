from PrimeNumberFunction import isPrime

start = True
for i in range(1,51):
    if isPrime(i) == True:
        if start == True:
            print(i,end ="")
            start = False
        else:
            print(", %s" %i, end= "")
