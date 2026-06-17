import json

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}

# # print(type(json.dumps(my_dict)))
# with open("mydic.json",'+a') as f:
#     json.dump(my_dict,f)

# with open("mydic.json",'+r') as f:
#     new_dic = json.load(f)
#     print(new_dic,type(new_dic))
    
import requests

resp = requests.get('https://jsonplaceholder.typicode.com/users')
if resp.status_code == 200:
    data_model = resp.json()
    # print(data_model)
    with open("test.json","+a") as f:
        json.dump(data_model,f)
        
