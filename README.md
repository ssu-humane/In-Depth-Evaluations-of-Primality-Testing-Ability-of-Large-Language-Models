![header](https://capsule-render.vercel.app/api?type=transparent&color=white&height=200&section=header&text=HUMANE_LAB&animation=blink&fontSize=50&fontColor=d6ace6)

# In-Depth Evaluations of Primality Testing Ability of Large Language Models
:octocat: 2047 개 수로 구성된 소수 및 합성수에 대한 난이도 별 검증 데이터셋을 함께 공개
## Dataset

데이터셋은 다음과 같이 구성되어 있습니다.

#### 소수 (prime number)
1. 2자리의 소수
2. 3자리의 소수
3. 4자리의 소수

#### 합성수 (composite number)
1. 2자리의 합성수
2. 3자리의 합성수 
3. 4자리의 합성수

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
|------|---|---|---|---|---|

