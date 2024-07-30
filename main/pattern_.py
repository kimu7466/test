# num = 5
# f_num = num+1
# for i in range(1, 5+1):
#     for j in range(5-i,0,-1):
#         print(" ", end=" ")
#     for j in range(i+1-1):
#         print("*", end=" ")
    # print()
    
# num = 5
# num += 1
# for i in range(num):
#     print(" "* (num-i), "* "*i)


# # Define the list of characters
# characters = ['@', '#', '$', '&']

# # Define the number of rows and columns in the pattern
# rows = 5
# columns = 4

# # Print the pattern
# for i in range(rows):
#     for j in range(columns):
#         if j == 0:
#             print(characters[0], end=' ')  # '@' in the first column
#         elif j == columns - 1:
#             print(characters[-1], end=' ')  # '&' in the last column
#         else:
#             # Choose characters from the middle of the list for other columns
#             print(characters[j], end=' ')
#     print()  # Move to the next line after printing each row













# # Define the list of characters
# characters = ['@', '#', '$', '&']

# # Define the height of the triangle
# height = 5

# # Print the triangle pattern
# for i in range(1, height + 1):
#     # Print spaces before the characters
#     print(' ' * (height - i), end='')
    
#     # Print characters for this row
#     for j in range(i):
#         if j == 0:
#             print(characters[0], end=' ')  # '@' in the first column
#         elif j == i - 1:
#             print(characters[-1], end=' ')  # '&' in the last column
#         else:
#             # Choose characters from the middle of the list for other columns
#             print(characters[j % (len(characters) - 2) + 1], end=' ')
    
#     # Move to the next line after printing each row
#     print()









# characters = ['@', '#', '$', '&']

# height = len(characters)

# for i in range(height):
#     for j in range(i + 1):
#         if j == 0:
#             print(characters[-1], end=' ')
#         else:
#             print(characters[j % (len(characters)) - 1], end=' ')
#         print()




# # Define the list of characters
# characters = ['@', '#', '$', '&']


# height = len(characters)
# for i in range(1,height+1):

#     for j in range(i):
#         if j == 0:
#             print(characters[j],end="_")
#         if j == 1:
#             print(characters[j],end="_")
#         if j == 2:
#             print(characters[j],end="_")
#         if j == 3:
#             print(characters[j],end="_")

#     print()


# characters = ['@', '#', '$', '&']

# for i in range(1, len(characters) + 1):
#     print(" ".join(characters[:i]))



# characters = ['&', '$', '#', '@']
# for i in range(len(characters)):
#     line = ""
#     for j in range(len(characters)):
#         if j >= len(characters) - i - 1:
#             line += characters[j]
#         else:
#             line += " "
#     print(line)


ch = ['&', '$', '#', '@']

for i in range(len(ch)):
    line = ""
    for j in range(i+1):
        line += ch[j] + " "
    print(line)


# for i in range(len(ch)):
#     line = ""
#     for j in range(len(ch)):
#         if j >= i :
#             line += ch[j-i] + " "
#         else:
#             line += ""
#     print(line)


# for i in range(len(ch)):
#     line = ""
#     for j in range(len(ch)):
#         if j >= len(ch)-i-1:
#             line += ch[j]+" "
#         else:
#             line += "  "

#     print(line)





# num = 5

# for i in range(num):
#     for j in range(num-i):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     for j in range(i):
#         print("*", end=" ")

#     print("")

# for i in range(num):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(num , i-1, -1):
#         print("*", end=" ")
#     for j in range(num , i, -1):
#         print("*", end=" ")

#     print("")




# ch = ['&', '$', '#', '@']
# ch = ['@', '#', '$', '&']

# for row in range(len(ch)):
#     print(" " * (len(ch) - row - 1), end="")
#     print("".join(ch[:row + 1][::-1]))

# num = chr(35)

# print (num)

# for i in range(30, 70):
#     print(chr(i))
"""
chr :|:  ord
____________
#   :|:  35
$   :|:  36 
%   :|:  37 
&   :|:  38
"""