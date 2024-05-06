list_items = [ 1, 2 ,3,4,5,6,7,8,9 ]

all_list_method = dir(list_items)
# print(type(list_items))
 
all_methods = []

for i in all_list_method :
    if i.startswith("__") :
        pass
    else:
        all_methods.append(i)

# print(all_methods)

for ind , i in enumerate(all_methods) :
    print(f"{ind+1} : {i}")

"""
1 : append
2 : clear
3 : copy
4 : count
5 : extend
6 : index
7 : insert
8 : pop
9 : remove
10 : reverse
11 : sort
"""
