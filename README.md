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

## Result

|제목|내용|설명|설명|설명|설명|설명|
|------|---|---|---|---|---|---|
|테스트1|Q1|Q2|Q3|Q4|Q5|Q6|
|테스트1|테스트2|테스트3|||||
|테스트1|테스트2|테스트3|||||
