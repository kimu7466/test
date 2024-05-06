# num = int(input("enter a number : "))
# num_list =[]
# for i in range(1,num+1):
#     # i = str(i)
#     num_list.append(i)
#     print(type(i))
# print(num_list)

def sum_list(*args):
    return sum(*args)

def multiply_list(*args):
    result = 1
    print(args)
    
    for num in args:
        for i in num:
            result *= i
    return result

lisst = [1, 2, 3, 4, 5]
print(multiply_list(lisst))
