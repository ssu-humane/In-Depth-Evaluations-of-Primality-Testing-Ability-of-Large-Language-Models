import openai
import random 
import json 
import os 
import re 

# 호출을 위한 키이다.
openai.api_key = "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"
# 호출하는 모델명이다. 
model = "gpt-3.5-turbo-0613"

# chatgpt api를 호출하늨 코드이다. 
# 질문을 넣으면 질문에 대한 답을 반환한다. 
def chatgpt(query):
    messages = [
            {"role": "system", "content": "You are a Maths solver."},
            {"role": "user", "content": query}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    answer = response['choices'][0]['message']['content']
    return answer 
# 이를 반복적으로 호출하여 각각의 프롬프트에 맞는 답변을 얻는다. 
# 연구에서 보고자 하는 것은 질문(프롬프트)에 따른 정확도 측정이다. 

# 아래 함수들은 사용의 편의를 위한 함수들이다. 

# 파일에 질문에 대한 답을 저장한다. 
def write_output(question, file_path):
    answer = chatgpt(question)
    answer = "###\n" + answer + "\n"
    f = open(file_path, "a", encoding="UTF-8")
    f.write(answer)
    f.close()
    # return answer

def return_file_path():
    output_file_lst = os.listdir("../output")
    output_file_lst = ["../output/"+ file for file in output_file_lst]
    yes_no_file_lst = os.listdir("../yes_no")
    yes_no_file_lst = ["../yes_no/"+ file for file in yes_no_file_lst]
    json_file_lst = os.listdir("../json")
    json_file_lst = ["../json_sampled/"+ file for file in json_file_lst]
    return output_file_lst, yes_no_file_lst, json_file_lst

def make_output(save_file, json_file):
    with open(json_file) as file:
        querys = json.load(file)
    q_len = len(querys[0])-2
    f = open(save_file, "a+t", encoding='UTF-8')
    # for restarting code 
    while True:
        try:
            f = open(save_file, "", encoding='UTF-8')
            text = f.read()
            x_idx = text.count("###") // q_len
            q_idx = text.count("###") %  q_len
            for query in querys[x_idx:]:
                query = list(query.values())[:-2]
                for question in query[q_idx:]:
                    write_output(question, save_file)
                q_idx = 0
            if x_idx >= len(querys):
                break 
        except:
            continue
    f.close()

def return_output(file_path, start_idx):
    f = open(file_path, "r", encoding='UTF-8') 
    text = f.read() 
    end_idx   = text.find("###", start_idx+1)
    output = text[start_idx:end_idx].replace("###", "")
    start_idx = end_idx
    f.close() 
    return output, start_idx

def return_json_data(file_path):
    with open(file_path) as file:
        querys = json.load(file)
    return querys

def return_PrimeOrComposite(output, i):
    output = re.sub('To determine if ([0-9]+|it) is a (prime|composite) number', ' ', output)
    # Since 29 is a prime number, If it is not divisible by 7, then 49 is a prime number.
    output = re.sub('Since [0-9]+ is a prime number,', ' ', output)
    output = re.sub('If it is not divisible by [0-9]+, then [0-9]+ is a prime number.', ' ', output)
    
    
    output = output.replace(".\n\n", ".").replace("\n", "")
    output_list = re.split("[.,]", output) 
    
    # print(output_list)
    temp_output = ""
    for i in range(1, len(output_list)+1):
        temp_output =  output_list[-i] + temp_output 
        # print(temp_output)
        # print(temp_output + "\n\n")
        prime_case_list = []
        prime_case_list.append(re.compile("([0-9]+|[iI]t) is (likely |indeed |actually |)(a prime number|prime)"))
        prime_case_list.append(re.compile("we( can|) conclude that (it |[0-9]+ )is (likely |indeed |)(a prime number|prime| prime number)"))
        prime_case_list.append(re.compile("it is (only|) divisible by 1 and itself"))
        prime_case_list.append(re.compile("does not have (any|) factors other than 1 and itself"))
        prime_case_list.append(re.compile("([0-9]+|[iI]t) is (likely|indeed|)not (a |)composite( number|)"))
        prime_case_list.append(re.compile("([0-9]+|[iI]t) is (likely |indeed |)a [pP]rime [nN]umber"))
        prime_case_list.append(re.compile("([0-9]+|[iI]t) can (only |)be divided (evenly |)by 1 and [0-9]+"))
        prime_case_list.append(re.compile("([0-9]+|[iI]t) can (only |)be expressed as a product of prime factors"))
        prime_case_list.append(re.compile("conclude that (it|[0-9]+) is [likely |indeed |]a prime number"))
        prime_case_list.append(re.compile("making (it|[0-9]+) a prime number"))
        prime_case_list.append(re.compile("does not have any factors other than 1 and itself"))
        prime_case_list.append(re.compile("([Ii]t|[0-9]+) (is|can be) (classified|considered) (as |)a prime number"))
        prime_case_list.append(re.compile("the number [0-9]+ is called a prime number"))
        prime_case_list.append(re.compile("([0-9]+|[Ii]t) is not divisible by any numbers other than 1 and itself"))
        prime_case_list.append(re.compile("([0-9]+|[Ii]t) is not divisible by any other numbers and is considered a prime number"))
        prime_case_list.append(re.compile("([0-9]+|[Ii]t) can be considered as a (potential |)prime number"))
        prime_case_list.append(re.compile("([0-9]+|[Ii]t) is categorized as a prime number"))
        prime_case_list.append(re.compile("([0-9]+|[Ii]t) does not have any prime factors and is a prime number"))
        prime_case_list.append(re.compile("([0-9]+|[Ii]t) is an example of a prime number and is not composite"))
        prime_case_list.append(re.compile("we can confirm that ([0-9]+|[Ii]t) is in fact a prime number"))
        
       
        
        composite_case_list = []
        composite_case_list.append(re.compile("([0-9]+|[iI]t) is (likely |indeed |)(|a )composite( number|)"))
        composite_case_list.append(re.compile("([0-9]+|[iI]t) is (likely |indeed |)(not|Not|NOT) a prime number"))
        # composite_case_list.append(re.compile("does not have any factors"))
        # composite_case_list.append(re.compile("([0-9]+|[iI]t) is not divisible"))
        composite_case_list.append(re.compile("([0-9]+|[iI]t) is divisible by a number"))
        composite_case_list.append(re.compile("([0-9]+|[iI]t) has factors other than 1 and itself"))
        composite_case_list.append(re.compile("making it a composite number"))
        composite_case_list.append(re.compile("([Ii]t|[0-9]+) is (classified|considered) (as |)a composite number"))
        composite_case_list.append(re.compile("([Ti]t|[0-9]+) has divisors other than 1 and itself"))
        composite_case_list.append(re.compile("([Ii]t|[0-9]+) has factors"))
        composite_case_list.append(re.compile("([Ii]t|[0-9]+) is divisible by more than"))
        composite_case_list.append(re.compile("([0-9]+|[Ii]t) is divisible by [0-9]+ and not a prime number"))
        composite_case_list.append(re.compile("([0-9]+|[Ii]t) cannot be a prime number"))
        composite_case_list.append(re.compile("([0-9]+|[Ii]t) is divisible by [0-9]+ and is therefore a composite number"))
        composite_case_list.append(re.compile("([0-9]+|[Ii]t) can't be a prime number"))
        composite_case_list.append(re.compile("making (it|[0-9]+) a composite number"))
        composite_case_list.append(re.compile("(it|[0-9]+) cannot be a prime number"))
        composite_case_list.append(re.compile("(it|[0-9]+) is divisible by [0-9]+ and is therefore a composite number"))
        
    
        for case1 in composite_case_list:
            if case1.search(temp_output):
                for case2 in prime_case_list:
                    if case2.search(temp_output):
                        # print(case1, case2)
                        return "idk" 
        for case in composite_case_list:
            if case.search(temp_output):
                return "composite"         
        for case in prime_case_list:
            if case.search(temp_output):
                return "prime"
        
    if (i==0 or i==1) and (re.search("[Yy]es", output)):
        return "prime"
    if (i==2 or i==3) and re.search("[Nn]o", output):
        return "composite"
    if (i==2 or i==3) and re.search("[Nn]o", output):
        return "prime"
    if (i==0 or i==1) and re.search("[Yy]es", output):
        return "composite"    
    
    
    return "idk"

def pretty_print(acc_list, data_type, len_q):
    acc_list = (acc_list / len_q) * 100
    print(f"{data_type}")
    for i in range(len(acc_list)):
        print(f"Q{i+1} acc : {acc_list[i]:.2f}")