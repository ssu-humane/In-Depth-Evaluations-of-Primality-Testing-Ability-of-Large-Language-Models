import openai
import random 
import json 
import os 
import re 

def return_output(file_path, start_idx):
    f = open(file_path, "r", encoding='UTF-8') 
    text = f.read() 
    end_idx   = text.find("###", start_idx+1)
    output = text[start_idx:end_idx].replace("###", "")
    start_idx = end_idx
    f.close() 
    return output, start_idx

def return_file_path():
    output_file_lst = os.listdir("../output")
    output_file_lst = ["../output/"+ file for file in output_file_lst]
    json_file_lst = os.listdir("../json")
    json_file_lst = ["../json_sampled/"+ file for file in json_file_lst]
    return output_file_lst, json_file_lst

def return_json_data(file_path):
    with open(file_path) as file:
        querys = json.load(file)
    return querys

def return_PrimeOrComposite(output, i):
    output_list = re.split("[.]", output) 
    
    # agree to the question
    if (i==0) and (re.search("[Yy]es", output)):
        return "prime"
    if (i==2) and re.search("[Yy]es", output):
        return "composite"
    # disagree to the question
    if (i==0) and re.search("[Nn]o", output):
        return "composite"
    if (i==2) and re.search("[Nn]o", output):
        return "prime"
    
    # agree to the question
    if (i==1) and (re.search("the final answer is [Yy]es", output)):
        return "prime"
    if (i==3) and re.search("the final answer is [Yy]es", output):
        return "composite"
    # disagree to the question
    if (i==1) and re.search("the final answer is [Nn]o", output):
        return "composite"
    if (i==3) and re.search("the final answer is [Nn]o", output):
        return "prime"

    # print(output_list)
    temp_output = ""
    for i in range(1, len(output_list)+1):
        temp_output =  output_list[-i] + temp_output 
        # print(temp_output)
        # print(temp_output + "\n\n")
        # the final answer is no
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
        # 1549 is not prime
        # 5281 is not divisible by 2, 3, 4, 5, 6, 8, 9, 10
        # 3931 is not divisible by 2, 3, 5, 7, 11, 13, 17
        # 1451 is divisible by 1, 1451, and
        composite_case_list.append(re.compile("[0-9]+ is divisible by 1, [0-9]+, and [0-9]+"))
        composite_case_list.append(re.compile("([0-9]+|[iI]t) is not prime"))
        composite_case_list.append(re.compile("([0-9]+|[iI]t) is divisible by 11"))
        composite_case_list.append(re.compile("([0-9]+|[iI]t) is divisible by ([^1]|[^1][0-9]+)"))
        composite_case_list.append(re.compile("([0-9]+|[iI]t) is (likely |indeed |)(|a )composite( number|)"))
        composite_case_list.append(re.compile("([0-9]+|[iI]t) is (likely |indeed |)(not|Not|NOT) a prime number"))
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
                        print(case1, case2, temp_output)
                        return "idk" 
                    
        for case in composite_case_list:
            if case.search(temp_output):
                return "composite"         
        for case in prime_case_list:
            if case.search(temp_output):
                return "prime"
        
    return "idk"

def pretty_print(acc_list, data_type, len_q):
    acc_list = (acc_list / len_q) * 100
    print(f"{data_type}")
    for i in range(len(acc_list)):
        print(f"Q{i+1} acc : {acc_list[i]:.2f}")