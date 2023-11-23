![header](https://capsule-render.vercel.app/api?type=transparent&color=white&height=200&section=header&text=HUMANE_LAB&animation=blink&fontSize=50&fontColor=d6ace6)

# In-Depth Evaluations of Primality Testing Ability of Large Language Models
:octocat: 2047 개 수로 구성된 소수 및 합성수에 대한 난이도 별 검증 데이터셋을 함께 공개
## Dataset

데이터셋은 다음과 같이 구성되어 있습니다.

#### 소수 (prime number)
1 소수 데이터 
1) 2 자리: 2 자리 소수 21 개
2) 2) 3 자리: 3 자리 소수 143 개
3) 4 자리: 4 자리 소수 500 개 

#### 합성수 (composite number)
2 합성수 데이터 
1) 2 자리: 2 자리 합성수 전체 (69 개)
2) 3 자리 쉬움: 가장 작은 인수의 크기가 10 이하인 3 자리 합성수 202 개
3) 4 자리 쉬움: 가장 작은 인수의 크기가 10 이하인 4 자리 합성수 500 개
4) 3 자리 중간: 가장 작은 인수의 크기가 10 이상 50 이하인 3 자리 합성수 56 개
5) 4 자리 중간: 가장 작은 인수의 크기가 10 이상 50 이하인 4 자리 합성수 500 개
6) 4 자리 어려움: 가장 작은 인수의 크기가 51 이상인 4 자리 합성수 56 개

## Expriment

#### 소수인 경우 질문
1. Is {number} a prime number? The answer is:
2. Is {number} a prime number? \nLet's think step by step
3. Is {number} a composite number? The answer is:
4. Is {number} a composite number? \nLet's think step by step

#### 합성수인 경우 질문
1. Is {number} a prime number? The answer is:
2. Is {number} a prime number? \nLet's think step by step
3. Is {number} a composite number? The answer is:
4. Is {number} a composite number? \nLet's think step by step
   
## Result

|제목|Q1 Acc|Q2 Acc|Q3 Acc|Q4 Acc|데이터 수|

표 1. 소수 데이터 정확도

소수 데이터 Q1 Q2 Q3 Q4
2 자리 100% 100% 100% 100%
3 자리 98.60% 100% 97.20% 95.80%
4 자리 70.20% 94.60% 25.40% 93.40%

표 2.
합성수 데이터 정확도

합성수 데이터 Q1 Q2 Q3 Q4
2 자리 100% 94.20% 68.12% 89.86%
3 자리 쉬움 93.07% 76.24% 84.16% 46.04%
4 자리 쉬움 87.40% 53.20% 91.80% 48.20%
3 자리 중간 91.07% 32.14% 94.64% 37.50%
4 자리 중간 32.20% 7.20% 81.20% 11.40%
4 자리 어려움 41.22% 7.63% 80.92% 8.40%
