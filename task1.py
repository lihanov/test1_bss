import json

def list_dict(dicts):
    global t    
    for i in dicts:
        x = dicts[i]
        y = (str(t) + str(i) + ': ' + str(x))
        if str(y).count(':') == 1:
            print(y)
            
        else:
            print(str(t) + str(i) + ':')
            t = '\t'
            for d in x:
                list_dict(d)
        
file = open('task3.json', encoding='utf-8')
data = json.load(file)
t = ''
list_dict(data)

