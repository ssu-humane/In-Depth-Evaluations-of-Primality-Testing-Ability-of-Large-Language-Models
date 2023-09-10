import openai
import random 
import json 
import os 

openai.api_key = "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"
model = "gpt-3.5-turbo-0613"

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
    json_file_lst = ["../json/"+ file for file in json_file_lst]
    return output_file_lst, yes_no_file_lst, json_file_lst

def make_output(save_file, json_file):
    with open(json_file) as file:
        querys = json.load(file)
    q_len = len(querys[0])-2
    f = open(save_file, "a+t", encoding='UTF-8')
    # for restarting code 
    while True:
        try:
            f = open(save_file, "r", encoding='UTF-8')
            text = f.read()
            x_idx = text.count("###") // q_len
            print(x_idx)
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