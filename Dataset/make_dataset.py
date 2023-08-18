import random 
import json

# 2 ~ 10000 : prime number
n = 10000
a = [False, False] + [True] * (n-1)
primes = [] 

for i in range(2, n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
      a[j] = False 

def make_json(file_name, primes):
  primes_dic = []
  for number in primes:
    q = {"question1":f"Is {number} a prime number?", 
        "question2":f"Is {number} a prime number? \nLet's think step by step.",
        "question3":f"Is {number} a composite number?",
        "question4":f"Is {number} a composite number? \nLet's think step by step.",
        #  "question5":f"Is 9791 divisible by 13? Answer with either Yes or No.",
        #  "question6":f"Is 9791 divisible by 13? Answer with either Yes or No.",
        "number": number,
        "answer":"prime",
        }
    primes_dic.append(q)
    
  json_data = json.dumps(primes_dic)
  with open(file_name, 'w') as f:
    f.write(json_data)

def make_json_composite(file_name, primes_list):
  primes_dic = []; factor1 = 0; factor2 = 0
  for number in primes_list:
    for prime in primes:
      if number % prime == 0:
        factor1 = int(number//prime)
        factor2 = prime
        # print(factor1*factor2, number)
    q = {"question1":f"Is {number} a prime number?", 
        "question2":f"Is {number} a prime number? \nLet's think step by step.",
        "question3":f"Is {number} a composite number?",
        "question4":f"Is {number} a composite number? \nLet's think step by step.",
        "question5":f"Is {number} divisible by {factor1}? Answer with either Yes or No.",
        "question6":f"Is {number} divisible by {factor2}? Answer with either Yes or No.",
        "number": number,
        "answer":"prime",
        }
    primes_dic.append(q)
  json_data = json.dumps(primes_dic)
  with open(file_name, 'w') as f:
    f.write(json_data)
    
# 1 ~ 10 : prime number
primes_10 = [number for number in primes if number < 10]
make_json("1_digit_prime.json", primes_10)

# 11 ~ 100 : prime number
primes_100 = [number for number in primes if (number < 100) and (number >= 10)]
make_json("2_digit_prime.json", primes_100)

# 101 ~ 1000 : prime number 
primes_1000 = [number for number in primes if (number < 1000) and (number >= 100)]
make_json("3_digit_prime.json", primes_1000)

# 1001 ~ 10000 : prime number
primes_10000 = [number for number in primes if (number < 10000) and (number >= 1000)]
make_json("4_digit_prime.json", primes_10000)

# 1 ~ 100 : composite number
composite_100 =  set([number for number in [i for i in range(1, 100)] if number not in primes_100])
make_json_composite("2_digit_composite.json", composite_100)

# 100 ~ 1000 : composite number 
# Easy : 1 ~ 10 * 11 ~ 1000
easy_composite_1000 = []
for number_10 in primes_10:
  for number_100 in primes_100:
    easy_composite_1000.append(number_10 * number_100)
  for number_1000 in primes_1000:
    easy_composite_1000.append(number_10 * number_1000)
easy_composite_1000 =  set([number for number in easy_composite_1000 if (number > 100) and (number < 1000)])
make_json_composite("3_digit_easy_composite.json", easy_composite_1000)

# 100 ~ 1000 : composite number 
# Medium :  11 ~ 50 * 11 ~ 100
medium_composite_1000 = []
for number_100 in primes_100:
  if number_100 <= 50:
    for number2_100 in primes_100:
      if number_100 != number2_100:
        medium_composite_1000.append(number_100 * number2_100)
medium_composite_1000 =  set([number for number in medium_composite_1000 if (number > 100) and (number < 1000)])
make_json_composite("3_digit_medium_composite.json", medium_composite_1000)

# 100 ~ 1000 : composite number 
# hard : 51 ~ * 51 ~ => Can't make it in this condition

# 1000 ~ 10000 : composite number
# Medium :11 ~ 51 * 51 ~ ?
easy_composite_10000 = []
for number in primes:
  if number < 10:
    for number2 in primes:
      # not square number
      if number2 > 10:
        if number != number2:
          easy_composite_10000.append(number * number2)
# 100 ~ 1000 
easy_composite_10000 = set([number for number in easy_composite_10000 if (number > 1000) and (number < 10000)])
make_json_composite("4_digit_easy_composite.json", easy_composite_10000)

# 1000 ~ 10000 : composite number
# Medium :11 ~ 51 * 51 ~ ?
medium_composite_10000 = []
for number in primes:
  if number < 50 and number >=10:
    for number2 in primes:
      # not square number
      if number2 > 10:
        if number != number2:
          medium_composite_10000.append(number * number2)
medium_composite_10000 =  set([number for number in medium_composite_10000 if (number > 1000) and (number < 10000)])
make_json_composite("4_digit_medium_composite.json", medium_composite_10000)

# 1000 ~ 10000 : composite number
# Hard :51 ~ * 51 ~ 
hard_composite_10000 = []
for number in primes:
  if number <= 50:
    continue 
  for number2 in primes:
    if number2 <= 50:
      continue 
    if number != number2:
      hard_composite_10000.append(number * number2)
hard_composite_10000 =  set([number for number in hard_composite_10000 if (number > 1000) and (number < 10000)])
make_json_composite("4_digit_hard_composite.json", hard_composite_10000)
