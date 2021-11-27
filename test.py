import http.client
import json
import time

conn = http.client.HTTPSConnection("api.surveymonkey.com")
token = "dnjl3jg6HVaCewgBLAcymiBI3LRQMeZXT39ekqq92hR.yIXAfmhx29BG.72drKkfsKy-9mlaesgcQSzM4j5OPGKo1oyTC0c3Abo1sTmgXjIMJrYU-qiOnw1BpExs4txa"
survey_id = "314966808"
page_id = "184352631"
headers = {
    'Accept': "application/json",
    'Authorization': "Bearer " + token
    }

"""
conn.request("GET", "/v3/surveys/"+survey_id+"/responses/bulk", headers=headers)

res = conn.getresponse()
data = res.read()
j = json.loads(data)
print(json.dumps(j, indent=4))
"""

response_id_list = []

#print(data.decode("utf-8"))


def get_response_plus_answers(dictionary_answers):
    url = "/v3/surveys/" + survey_id + "/responses/bulk"
    conn.request("GET", url, headers=headers)
    response = conn.getresponse()
    data = response.read()
    jsn = json.loads(data)
    dic = {}
    
    for i in range (len(jsn["data"])):
        #print(jsn["data"][i]["id"])
        person = jsn["data"][i]["id"]
        dic[person] = []
        for j in range (len(jsn["data"][i]["pages"][0]["questions"])):
            
            res = []
            #print(jsn["data"][i]["pages"][0]["questions"][j])
            ans = jsn["data"][i]["pages"][0]["questions"][j]["answers"]
            
            for d in ans:
                a = d["choice_id"]
                res.append(dictionary_answers[a])
                if a not in response_id_list:

                    response_id_list.append(d["choice_id"])

            #print("Antworten: ", res)
            
            dic[person].append(res)
    
    print(json.dumps(dic, indent=4, ensure_ascii=False))
    return dic

def get_response_names(liste):
    for i in liste:
        i = int(i)
        url = f"/v3/surveys/{survey_id}/responses/{i}/details" 
        conn.request("GET", url, headers=headers)
        response = conn.getresponse()
        data = response.read()
        jsn = json.loads(data)
        print(json.dumps(jsn, indent=4))
        time.sleep(0.5)

        
def get_quest_ids():
    quest_id_list = []
    url = f"/v3/surveys/{survey_id}/pages/{page_id}/questions"
    conn.request("GET", url, headers=headers)
    response = conn.getresponse()
    data = response.read()
    jsn = json.loads(data)

    for i in jsn["data"]:
        quest_id_list.append(i["id"])

    
    return (quest_id_list)

def get_answers_in_text(quest_list):
    dic_answers = {}
    for i in quest_list:
        time.sleep(0.5)
        url = f"/v3/surveys/{survey_id}/pages/{page_id}/questions/{i}"
        conn.request("GET", url, headers=headers)
        response = conn.getresponse()
        data = response.read()
        jsn = json.loads(data.decode("utf-8"))

        for j in jsn["answers"]["choices"]:
            
            text = j["text"]
            id = j["id"]
            dic_answers[id] = text

    
    
    return dic_answers


#get_response_plus_answers()
#print(response_id_list)
#get_response_names(response_id_list)

dictionary_answers = get_answers_in_text(get_quest_ids())
get_response_plus_answers(dictionary_answers)