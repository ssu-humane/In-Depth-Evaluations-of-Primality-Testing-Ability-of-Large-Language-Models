import utils 
import numpy as np 
import pandas as pd 
import warnings 
import csv 


warnings.filterwarnings('ignore')
fields = ['query', 'output', 'result']
save_file = []
text_files, json_files = utils.return_file_path() 
cnt = 0
idk_cnt = 0

composite_acc = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
composite_query_cnt = [0, 0, 0]
acc_dict = {}

for text_file, json_file in zip(text_files, json_files):
    output = "" 
    start_idx = 0 
    q_cnt=0
    q_idk_cnt=0
    number_type = ("prime" if "prime" in text_file else "composite")
    data_type = json_file.rstrip(".json").lstrip("../json_sampled/")
    querys = utils.return_json_data(json_file) 
    acc = np.array([0, 0, 0, 0])
    
    for query in querys:
        query = list(query.values())
        for i in range(len(query)-2):
            output, start_idx = utils.return_output(text_file, start_idx)
            
            if i >= 4:
                continue
            
            result = utils.return_PrimeOrComposite(output, i)
            # print("\n", query[i], output, result, "\n")
                    
            if result == "idk":
                idk_cnt += 1
                # print("=========I Dont Know This Case=============")
                # print("\n", query[i], output, result, "\n")
                q_idk_cnt+=1
            q_cnt+=1
            cnt += 1
                
            if (result == "prime") and (number_type == "prime"):
                acc[i] += 1
            elif (result == "composite") and (number_type == "composite"):
                acc[i] += 1
                
            save_file.append([query[i], output, result])

    utils.pretty_print(acc_list=acc, data_type=data_type, len_q=len(querys))

    if number_type == "composite":
        # print(data_type)
        if data_type[0] == "2":
            composite_acc[0] += acc 
            composite_query_cnt[0] += len(querys)
        elif data_type[0] == "3":
            composite_acc[1] += acc 
            composite_query_cnt[1] += len(querys)
        elif data_type[0] == "4":
            composite_acc[2] += acc
            composite_query_cnt[2] += len(querys)
                         
for i in range(len(composite_acc)):
    composite_acc[i] = (composite_acc[i] / composite_query_cnt[i]) * 100

for acc_list in composite_acc:
    for i in range(len(acc_list)):
        print(f"Q{i+1} acc : {acc_list[i]:.2f}")

# print(idk_cnt / cnt * 100)
# with open('sampling_script.csv', 'w', encoding="utf-8") as f:
     
#     # using csv.writer method from CSV package
#     write = csv.writer(f)
     
#     write.writerow(fields)
#     write.writerows(save_file)