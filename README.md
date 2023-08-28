![header](https://capsule-render.vercel.app/api?type=transparent&color=white&height=200&section=header&text=HUMANE_LAB&animation=blink&fontSize=50&fontColor=d6ace6)



# GPT-reasoning-prompting
:octocat: Repository for data and code that tests the reasoning ability of the GPT model.

## I USED
<img src="https://img.shields.io/badge/python-3776AB?style=flat-square&logo=Python&logoColor=white"/> 

## It is started by
How Language Model Hallucinations Can Snowball : https://arxiv.org/abs/2305.13534

In my opinion, I thought that the dataset in this paper would be biased because it is a dataset with only yes or no.

## Dataset

데이터셋은 다음과 같이 구성되어 있습니다.

#### 소수 (prime number)
1. 2자리의 소수
2. 3자리의 소수
3. 4자리의 소수

#### 합성수 (composite number)
1. 2자리의 합성수
2. 3자리의 합성수 
<br> <br> 2-1. 10 이하의 수 * a
<br> <br> 2-2. 50 이하의 수 * a

3. 4자리의 합성수
<br> <br> 3-1. 10이하의 수 * a
<br> <br> 3-2. 50이하의 수 * a
<br> <br> 3-3. 50이상의 수 * a 

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
5. Is {number} divisible by {factor1}? Answer with either Yes or No.
6. Is {number} divisible by {factor2}? Answer with either Yes or No.
   
#### Yes/No 추출하기
- (앞에서 한 질문의 output) + (앞에서 한 질문 [stey by step은 replace ""]) + "\nAnswer with either Yes or No.") ["###"제거]

## Result

|제목|Q1 Acc|Q2 Acc|Q3 Acc|Q4 Acc|Q5 Acc|Q6 Acc|데이터 수|
|------|---|---|---|---|---|---|---|
|2자리의 소수|100.0|100.0|100.0|100.0|||21|
|3자리의 소수|98.6|100.0|97.2|94.4|||143|
|4자리의 소수|96.8|93.8|25.8|69.8|||500|
|2자리의 합성수|100.0|100.0|89.9|89.9|98.6|92.7|69|
|3자리의 합성수 [10 이하의 수 * a]| 97.0|79.7|92.5| 69.8|70.2|61.8|202|
|3자리의 합성수 [50 이하의 수 * a]|92.8|60.7| 96.4|46.4| 71.4| 53.5|56|
|4자리의 합성수 [10 이하의 수 * a]| 89.2|79.4| 94.8|63.4|88.6|80.4|500|
|4자리의 합성수 [50 이하의 수 * a]|24.4|19.0| 77.2| 24.0|80.4|55.6|500|
|4자리의 합성수 [50 이상의 수 * a]| 37.4|8.3| 74.8|27.4|75.5| 83.9|56|
