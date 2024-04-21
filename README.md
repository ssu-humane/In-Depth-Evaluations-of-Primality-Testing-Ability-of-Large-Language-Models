![header](https://capsule-render.vercel.app/api?type=transparent&color=white&height=200&section=header&text=HUMANE_LAB&animation=blink&fontSize=50&fontColor=d6ace6)

# 대규모 언어 모델의 소수 검증 능력 심층 평가: ChatGPT와 PaLM 2를 중심으로

이 저장소는 "대규모 언어 모델의 소수 검증 능력 심층 평가: ChatGPT와 PaLM 2를 중심으로"라는 제목의 논문에 사용된 데이터셋과 코드를 포함하고 있습니다.

## 사용된 프롬프트

연구에서는 일반적인 프롬프트(Q1, Q2)와 추론 과정을 생성하는 Chain-of-Thoughts 프롬프트(Q3, Q4)를 사용하였습니다.

- Q1: "Is {number} a prime number? The answer is:"
- Q2: "Is {number} a composite number? The answer is:"
- Q3: "Is {number} a prime number? Let's think step by step."
- Q4: "Is {number} a composite number? Let's think step by step."

## 소수 검증 결과 (표 1)

| Type | w/o CoT |  | w/ CoT |  |
|------|---------|--|--------|--|
|      | ChatGPT | PaLM2 | ChatGPT | PaLM2 |
| 2 digits | 1 | 0.667 | 1 | 0.476 |
| 3 digits | 0.958 | 0.7 | 0.958 | 0 |
| 4 digits | 0.209 | 0 | 0.884 | 0 |

- ChatGPT는 CoT 프롬프트 사용 시 4자리 소수에 대한 정확도가 크게 향상되었습니다.
- PaLM 2는 3자리와 4자리 소수에 대해 대부분 합성수로 판단하는 경향을 보였습니다.

## 합성수 검증 결과 (표 2)

| Type | w/o CoT |  | w/ CoT |  |
|------|---------|--|--------|--|
|      | ChatGPT | PaLM2 | ChatGPT | PaLM2 |
| 2 digits | 0.681 | 0.971 | 0.841 | 0.826 |
| 3 digits easy | 0.807 | 0.807 | 0.485 | 0.807 |
| 4 digits easy | 0.816 | 0.988 | 0.292 | 0.996 |
| 3 digits medium | 0.893 | 0.536 | 0.107 | 0.714 |
| 4 digits medium | 0.292 | 0.93 | 0.016 | 0.986 |
| 4 digits hard | 0.374 | 0.931 | 0.76 | 1 |

- PaLM 2가 ChatGPT보다 합성수 검증에서 높은 성능을 보였습니다.
- CoT 프롬프트 사용 시 PaLM 2의 정확도가 대부분 향상되었습니다.

## 합성수 나눗셈 연산 오류율 (표 3)

| Type | w/ CoT |  |
|------|--------|--|
|      | ChatGPT | PaLM2 |
| 2 digits | 0.035 | 0.404 |
| 3 digits easy | 0.225 | 0.951 |
| 4 digits easy | 0.363 | 0.968 |
| 3 digits medium | 0.667 | 1 |
| 4 digits medium | 1 | 0.996 |
| 4 digits hard | 1 | 1 |

- 난도가 증가함에 따라 두 모델 모두 나눗셈 연산 오류율이 증가하였습니다.
- 4자리 합성수에 대해서는 모든 추론 과정에서 나눗셈 연산 오류가 발생하였습니다.

## 연구 결과 요약

- 가설 1 지지: 소수를 대상으로 한 검증에서, 자릿수가 증가함에 따라 정확도가 감소하는 경향을 보였습니다.
- 가설 2 일부 지지: 연산 오류율을 반영한 Chain-of-Thoughts 검증 정확도에서, 가장 작은 약수 크기 증가에 따라 정확도가 감소하였습니다.
- 가설 3 지지: 가장 작은 약수 크기가 증가함에 따라 나눗셈 연산 오류율이 증가하는 경향을 보였습니다.

연구 결과는 단순한 질문에 기반한 성능 벤치마크가 언어 모델 능력을 잘못 평가할 수 있으며, 특정 능력을 다각도로 평가하는 심층 분석이 필요함을 시사합니다.

## 기여 및 피드백

이 프로젝트에 대한 기여와 피드백을 환영합니다. 연구 내용이나 코드에 대한 제안이 있다면 이슈를 생성하거나 Pull Request를 보내주시기 바랍니다.
