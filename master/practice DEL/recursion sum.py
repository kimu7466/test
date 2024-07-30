# question 1:  sum all the number in list with recursion.
num_list = [1,2,3,4,5,6]

# print(len(num_list)-1)

# print(num_list[1:])


# def sum_list(num_list):
#     if not sum_list(len(sum_list)):
#     sum = 0
#     return sum += sum_list() 


# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num-1)
    
# print(factorial(5))


num_list = [1, 2, 3, 4, 5]



def sum_list(lst):
    print("i am in")
    if not lst:  # Base case: If the list is empty, return 0
        print("not lst")
        return 0
    else:
        # print(f"****{lst[0]}****")
        return lst[0] + sum_list(lst[1:])  # Add the first element to the sum and recursively call sum_list with the rest of the list

# Test the function
result = sum_list(num_list)
print("Sum of all numbers in the list:", result)
# sum_list(num_list)

