import csv

fields = ["name","age","gender"]
rows =[
   {"name":"Magret","age":19,"gender":"female"}, 
   {"name":"Mark","age":17,"gender":"male"}, 
   {"name":"Jerry","age":18,"gender":"male"}, 
   {"name":"Jesse","age":18,"gender":"female"}, 
   {"name":"Beckey","age":18,"gender":"female"}, 
] 

# write data
# with open("person.csv",mode='w',encoding='utf-8-sig',newline='') as f:
#     writer = csv.DictWriter(f,fieldnames=fields)
#     # write the header
#     writer.writeheader()
#     writer.writerows(rows)

# read data,method1
with open("person.csv",mode='r',encoding='utf-8-sig',newline='') as f:
    reader = csv.DictReader(f) # when creater a reader object,fieldnames is not necessary
    print(list(reader)) # [{'name': 'Magret', 'age': '19', 'gender': 'female'}, {'name': 'Mark', 'age': '17', 'gender': 'male'}, {'name': 'Jerry', 'age': '18', 'gender': 'male'}, {'name': 'Jesse', 'age': '18', 'gender': 'female'}, {'name': 'Beckey', 'age': '18', 'gender': 'female'}]
    for r in reader: # the DictReader object is iterable,it has the data
        print(r) # each line will become a dict object
        
# read data,method2 ->return list
# with open("person.csv",mode='r',encoding='utf-8-sig',newline='') as f:
#     reader = csv.reader(f)
#     print(list(reader)) # 2 dimension list
#     for row in reader:
#         print(row) # each line will become a list
