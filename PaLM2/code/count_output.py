import utils 
import numpy as np 
import pandas as pd 
import warnings 
import csv 


warnings.filterwarnings('ignore')
#save_file =  pd.DataFrame(columns=['query', 'output', 'result'])
fields = ['query', 'output', 'result']
save_file = []
text_files, json_files = utils.return_file_path() 
cnt = 0
idk_cnt = 0

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
            # return output 함수가 이상한 것 같기도? # 질문이랑 맞는지 확인해야함.
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
    
    
    print(f"\nidk rate:{q_idk_cnt / q_cnt * 100}%")
    print(f"idk cnt:{q_idk_cnt} / {q_cnt}")
    print(f"q cnt: {q_cnt//4}\n")



print(f"\ntotal idk rate:{idk_cnt / cnt * 100}%")
print(f"total idk cnt:{idk_cnt} / {cnt}")
print(f"total cnt: {cnt//4}\n")
# with open('sampling_script.csv', 'w', encoding="utf-8") as f:
     
#     # using csv.writer method from CSV package
#     write = csv.writer(f)
     
#     write.writerow(fields)
#     write.writerows(save_file)