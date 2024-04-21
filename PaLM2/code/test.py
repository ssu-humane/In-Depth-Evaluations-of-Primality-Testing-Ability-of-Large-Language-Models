import utils

test_case2 = """"
5771 is divisible by 1, 5771, and 19.
"""
test_case = '''
4141 is divisible by 1, 4141, and 11. So, 4141 is not a prime number.
'''
number = 4141
        
if test_case.rfind("is divisible by") != -1:
    cut_output = test_case[test_case.rfind("is divisible by")+len("is divisible by")+1:]
    cut_output = cut_output.split(".")[0]
    cut_output = cut_output.replace("and", ",")
    cut_output = cut_output.replace(" , ", "") 
    cut_output = cut_output.replace("itself", f"{number}")
    
    print(cut_output)
    try: 
        num_list = list(map(int, cut_output.split(",")))
    except:
        if cut_output[-3] == ",":
            cut_output = cut_output[:-5]
            num_list = list(map(int, cut_output.split(",")))
    print(cut_output)
    
    # num_list = list(map(int, cut_output.split(",")))
    print(num_list)
    for factor in num_list:
        if (number%factor)==0:
            continue
        else:
            print("EEEERRRRR")
