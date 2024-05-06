# def getting():
#     x = int(input("enter a range : "))


#     for i in range(x):
#         if i == 0 or i == 1:
#             print(i)
#         else:
#             print()
    

     
# def fibonacci(n):
#     fib_sequence = [0, 1]
#     for i in range(2, n):
#         next_number = fib_sequence[-1] + fib_sequence[-2]
#         fib_sequence.append(next_number)
#     return fib_sequence

# # Example usage:
# n = 10  # Change n to the number of Fibonacci numbers you want
# print(fibonacci(n))



def fib_series(n):
    fib_list = [0, 1]
    for i in range(2,n):
        next_number = fib_list[-1]+fib_list[-2]
        fib_list.append(next_number)
    for num in fib_list:
        print(num)

n = 10
fib_series(10)
