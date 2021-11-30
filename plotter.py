import matplotlib.pyplot as plt
import pandas as pd
import json

#data = [100, 120, 140, 180, 200, 210, 214]
#s = pd.Series(data, index=range(len(data)))
#s.plot(kind="bar", rot=0)
#plt.show()



j = {}

with open("response_data.json", "r") as file:
    data = file.read()
    j = json.loads(data)
    
#print(json.dumps(j, indent=4, ensure_ascii=False))

def split_dic_ages(dic: dict):
    
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
    
    
    return [age_18_24, age_25_34, age_35_44, age_over_45]
    
def plot_hours_ages(liste):
    ages = ["18-24", "25-34", "35-44", "45+"]
    hours = [0,0,0,0]
    
    for i in range(len(liste)):
        counter = 0
        dic = liste[i]
        number = len(dic.keys())
        
        for key in dic.keys():
            #print(dic[key][3])
            if dic[key][3][0] == "0-2 Stunden":
                counter += 1
            if dic[key][3][0] == "2-4 Stunden":
                counter += 3
            if dic[key][3][0] == "4-6 Stunden":
                counter += 5
            if dic[key][3][0] == "ueber 6 Stunden":
                counter += 7
        counter = counter / number
        hours[i] = counter
        
    
    print(hours)
    s = pd.Series(hours, index=ages)
    s.plot(kind="bar", rot=0)
    
    plt.xlabel('Altersgruppen')
    plt.ylabel('Stunden pro Tag')
    plt.show()
    
    return

def plot_hours_by_sex(liste):
    ages = ["Männlich", "Weiblich"]
    hours = [0,0]
    
    for i in range(len(liste)):
        counter = 0
        dic = liste[i]
        number = len(dic.keys())
        
        for key in dic.keys():
            #print(dic[key][3])
            if dic[key][3][0] == "0-2 Stunden":
                counter += 1
            if dic[key][3][0] == "2-4 Stunden":
                counter += 3
            if dic[key][3][0] == "4-6 Stunden":
                counter += 5
            if dic[key][3][0] == "ueber 6 Stunden":
                counter += 7
        counter = counter / number
        hours[i] = counter
        
    
    print(hours)
    s = pd.Series(hours, index=ages)
    s.plot(kind="bar", rot=0)
    
    plt.xlabel('Geschlecht')
    plt.ylabel('Stunden pro Tag')
    plt.show()
    
    return

def split_sex(dic: dict):
    male = {}
    female = {}
    
    for key in dic.keys():
        if dic[key][0][0] == "Maennlich":
            male[key] = dic[key]
        elif dic[key][0][0] == "Weiblich":
            female[key] = dic[key]
            
            
    return [male, female]

def plot_activities_by_sex(liste):
    acties = ["Chatten",
            "Musik",
            "Social Media",
            "Filme",
            "Telefonieren",
            "Fotografieren",
            "Lesen",
            "Sonstiges"]
    
    male_acts = [0,0,0,0,0,0,0,0]
    female_acts = [0,0,0,0,0,0,0,0]
    
    
    dic = liste[0]
    for key in dic.keys():
        acts = dic[key][4]
        if "Chatten" in acts:
            male_acts[0] += 1
        if "Musik" in acts:
            male_acts[1] += 1
        if "Social Media" in acts:
            male_acts[2] += 1
        if "Filme" in acts:
            male_acts[3] += 1
        if "Telefonieren" in acts:
            male_acts[4] += 1
        if "Fotografieren" in acts:
            male_acts[5] += 1
        if "Lesen" in acts:
            male_acts[6] += 1
        if "Sonstiges" in acts:
            male_acts[7] += 1
            
    dic2 = liste[1]
    for key in dic2.keys():
        acts = dic2[key][4]
        if "Chatten" in acts:
            female_acts[0] += 1
        if "Musik" in acts:
            female_acts[1] += 1
        if "Social Media" in acts:
            female_acts[2] += 1
        if "Filme" in acts:
            female_acts[3] += 1
        if "Telefonieren" in acts:
            female_acts[4] += 1
        if "Fotografieren" in acts:
            female_acts[5] += 1
        if "Lesen" in acts:
            female_acts[6] += 1
        if "Sonstiges" in acts:
            female_acts[7] += 1
            
    print(male_acts)
    
    print(female_acts)
    
    for i in range(len(male_acts)):
        male_acts[i] = (male_acts[i] / len(dic.keys()))*100
        
    for i in range(len(female_acts)):
        female_acts[i] = (female_acts[i] / len(dic2.keys()))*100
        
    
    
    male_series = pd.Series(male_acts, index=acties)
    female_series = pd.Series(female_acts, index=acties)
    
    dataFrame = pd.DataFrame({"Männer":male_series, "Frauen":female_series})
    ax = dataFrame.plot.bar(color=["SkyBlue", "IndianRed"])
    plt.ylabel("Prozent")
    plt.show()
    
    #anzahl in listen durch anzahl männer/frauen teilen
    
        
            
    
        
         
            
    
           

l = split_dic_ages(j)
#plot_hours_ages(l)
k = split_sex(j)
plot_hours_by_sex(k)
#plot_activities_by_sex(k)