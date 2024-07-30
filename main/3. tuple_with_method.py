tuple_name = (1, 2, 3, 4, 5, 6, 7, 8, 9)  

tuple_list = dir(tuple_name)

tuple_method = []

for i in tuple_list :
    if i.startswith("__") :
        pass
    else:
        tuple_method.append(i)

# print(tuple_method)

for ind , i in enumerate(tuple_method) :
    print(f"{ind+1} : {i}")

"""
1 : count
2 : index
"""









