# def sum_list_recursive(lst):
#     # Base case: if the list is empty, return 0
#     if not lst:
#         return 1
#     # Recursive case: add the first element to the sum of the rest of the list
#     else:
#         # print(lst[0],"****")
#         return lst[0] * sum_list_recursive(lst[1:])


# x= int(input("enter a number to print it's factorial : "))

# # Example usage:
# my_list = [x for x in range(1,x+1)]
# print("Sum of the list:", sum_list_recursive(my_list))





















def recursive_factorial(lst):
    if not lst:
        return 1
    else:

        return lst[0] * recursive_factorial(lst[1:])
    
x = int(input("enter a number to find it's factorial : "))

num_list = [x for x in range(1,x+1)]
print(num_list)

fact = recursive_factorial(num_list)

print(f"the factorial of number {x} is {fact}.")





def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
