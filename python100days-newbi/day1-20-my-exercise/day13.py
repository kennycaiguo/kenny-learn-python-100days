"""
dict -》 similar to json,key-value pair
inside a dict ,there is a dict_keys collection and a dict_values collection and dict_items collection
dict.keys() ->dict_keys collection
dict.values() =>dict_values collection
dict.items() => dict_items collection
"""

man ={"name":"keny","age":18,"gender":"male"}
print(type(man)) # <class 'dict'>
# keys->method
print(man.keys) #<built-in method keys of dict object at 0x000001F2FA854900>
print(man.keys()) # dict_keys(['name', 'age', 'gender']) can be converted into list 
# values()
print(man.values()) # dict_values(['keny', 18, 'male'])
# items()
print(man.items()) # dict_items([('name', 'keny'), ('age', 18), ('gender', 'male')])

dic = dict()
print(dic) # {}
dic["name"] = "Jackline"
dic["age"] = 25
dic['job'] = 'secretary'
print(dic) # {'name': 'Jackline', 'age': 25, 'job': 'secretary'}

woker_info = [('name', 'Bob'), ('age', 30), ('gender', 'male')]
worker = dict(woker_info)
print(worker) # {'name': 'Bob', 'age': 30, 'gender': 'male'}

# iteration
for k,v in worker.items():
    print(f"{k}={v}",end=",")
print()    

# Dictionary Comprehension
dic2 = {x[0]:x[1] for x in woker_info} # not recommended
print(dic2) # {'name': 'Bob', 'age': 30, 'gender': 'male'}
dic3 = {k : v for (k,v) in woker_info}
print(dic3) # {'name': 'Bob', 'age': 30, 'gender': 'male'}
# in opertator
print("name" in dic3.keys()) # True
print("Bob" in dic3.values()) # True
print(("name","Bob") in dic3.items()) # True

# to change the value
dic3["job"] = "accountant"
print(dic3) # {'name': 'Jason', 'age': 30, 'gender': 'male', 'job': 'accountant'}
dic3["name"] = "Jason"
print(dic3)
# delete a key-value pair
del(dic3["job"])
print(dic3) # {'name': 'Jason', 'age': 30, 'gender': 'male'}
# pop(key)
popped = dic3.pop("age") # return the value of a key
print(dic3) # {'name': 'Jason', 'gender': 'male'}
print(popped) # 30, only the value
p_item = dic3.popitem() # return a key-value pair
print(dic3)
print(p_item) # ('gender', 'male')
# get(key) -> query value from a key
print(dic2.get('gender')) # male
print(dic["name"]) # Jackline
# print(dic['money']) # KeyError: 'money'
print(dic.get("money","Not found")) # Not found,the get(key) is safer than the dic[key]
# dict1.update(dict2) => expand dict1 with dict2
person = {'name': '王大锤', 'age': 55, 'height': 178}
info = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
# person.update(info)
person |= info # python 3.9 and up
print(person) # {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}

