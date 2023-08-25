import openai

openai.api_key = "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"
model = "gpt-3.5-turbo"

# 질문 작성하기
query = "안녕하세요"

def chatgpt(query):
    
    # 메시지 설정하기
    messages = [
            {"role": "system", "content": "You are a Maths solver."},
            {"role": "user", "content": query}
    ]

    # ChatGPT API 호출하기
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    answer = response['choices'][0]['message']['content']
    # print(answer)
    return answer 

def write_output(question, file_path):
    answer = chatgpt(question)
    answer = "###\n" + answer + "\n"
    f = open(file_path, "a", encoding="UTF-8")
    f.write(answer)
    f.close()