import matplotlib.pyplot as plt
import pandas as pd
import json
"""
data = [100, 120, 140, 180, 200, 210, 214]
s = pd.Series(data, index=range(len(data)))
s.plot(kind="bar", rot=0)
plt.show()


"""
j = {}

with open("response_data.json", "r") as file:
    data = file.read()
    j = json.loads(data)
    
#print(json.dumps(j, indent=4, ensure_ascii=False))

def split_dic_ages(dic: dict):
    print(len(dic.keys()))
    c = 0
    age_18_24  = {}
    age_25_34 = {}
    age_35_44 = {}
    age_over_45 = {}
    for i in dic.keys():
        if dic[i][1][0] == "18 bis 24":
            age_18_24[i] = dic[i]
        
        if dic[i][1][0] == "25 bis 34":
            age_25_34[i] = dic[i]
            
        if dic[i][1][0] == "35 bis 44":
            age_35_44[i] = dic[i]
            
        if dic[i][1][0] == "ueber 45":
            age_over_45[i] = dic[i]
    
    
        
            
    
           

split_dic_ages(j)