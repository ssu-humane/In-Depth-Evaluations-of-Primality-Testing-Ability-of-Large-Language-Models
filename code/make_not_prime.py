import random

n= 10000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
        
primes = [prime for prime in primes if prime > 50]

candidates = []

for prime in primes:
    for prime2 in primes:
        candidates.append(prime*prime2)

candidates = list(set(candidates))
candidates = sorted(candidates)
candidates = [candidate for candidate in candidates if  candidate < 50000]
candidates = random.sample(candidates, k=500)

# print(candidates)
candidates_dic = []
for candidate in candidates:
    q = {"question": f"Is {candidate} a prime number?", "number": candidate, "answer": False}
    candidates_dic.append(q)

# print(candidates_dic)

import json

json_data = json.dumps(candidates_dic)
with open('not_primality_testing.json', 'w') as f:
    f.write(json_data)