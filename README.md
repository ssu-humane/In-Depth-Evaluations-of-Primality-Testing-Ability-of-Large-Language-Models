![header](https://capsule-render.vercel.app/api?type=transparent&color=white&height=200&section=header&text=HUMANE_LAB&animation=blink&fontSize=50&fontColor=d6ace6)

# In-Depth Evaluations of Primality Testing Ability of Large Language Models
:octocat: 대규모 언어 모델은 다양한 언어 기반 작업에서 뛰어난 성능을 보이고 있으나, 수학적 추론 작업은 언어 모 델이 여전히 어려움을 겪고 있는 분야이다. 이 연구는 대규모 언어 모델의 수학적 추론 능력을 소수 검증 문제 에 대해 심층 분석한다. 일부의 소수 데이터만을 활용해 추론 분석을 수행했던 이전 연구와 다르게, 이 연구에 서는 합성수를 포함해 다양한 난이도의 데이터셋을 구성하여 ChatGPT 모델의 성능을 분석했다. 실험 결과, 합 성수를 대상으로 했을 때 소수를 대상으로 하는 것에 비해 풀이 정확도가 감소하며, 추론 과정을 명시적으로 생성하는 “Let’s think step by step” 프롬프트를 사용하였을 때 그 감소폭은 더 커짐을 관측하였다. 이는 언어 모델의 소수 풀이 능력이 사전학습 웹 데이터에 존재하는 정답과 풀이에 편향되었을 수 있음을 시사하는 결과 이다. 이 연구 결과는 대규모 언어 모델의 수학적 추론 능력을 검증하기 위한 중요한 기반이 될 것으로 기대하 며, 2047 개 수로 구성된 소수 및 합성수에 대한 난이도 별 검증 데이터셋을 함께 공개한다.
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

