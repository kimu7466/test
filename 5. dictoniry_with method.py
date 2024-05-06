my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

dict_list = dir(my_dict)

dict_method = []

for i in dict_list:
    if i.startswith("__"):
        pass
    else:
        dict_method.append(i)

# print(dict_method)
        
for ind, i in enumerate(dict_method):
    print(f"{ind+1} : {i}")


""" 
1 : clear
2 : copy
3 : fromkeys
4 : get
5 : items
6 : keys
7 : pop
8 : popitem
9 : setdefault
10 : update
11 : values 
"""