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



for i in all_methods :
    print(i)











