import random

n= 10000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
        
primes_10 = [prime for prime in primes if prime < 10]

print(primes_10)

primes_50 = [prime for prime in primes if (prime >= 10) and (prime < 50) ]

print(primes_50)

primes_51 = [prime for prime in primes if (prime >= 50)and (prime < 1000)]

print(primes_51)

primes_100 = [prime for prime in primes if (prime >= 1) and (prime < 100) ]

print(primes_100)

primes_1000 = [prime for prime in primes if (prime >= 100) and (prime < 1000) ]

print(primes_100)

primes_10000 = [prime for prime in primes if (prime >= 1000) and (prime < 10000) ]

print(primes_10000)