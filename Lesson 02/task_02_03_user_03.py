def primes():
    num=2
    while True:
        for i in range(num-1,1,-1):
            if num%i==0: break
        else: yield num
        num+=1

# n = 10**4 Elapsed time: 4.843 sec