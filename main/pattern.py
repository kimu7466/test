


num = 5 

# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()


# for i in range(num, 0, -1):
#     print("* "*i)

k = ord("A")

# for i in range(num):
#     for j in range(i+1):
#         print(chr(k), end=" ")
#         k += 1
#     print()


# for i in range (num):
#     for j in range(i+1):
#         if j % 2 == 0:
#             print(1, end= " ")
#         else:
#             print(0, end= " ")

#     print()



# for i in range(num):
#     for j in range(i):
#         print("_",end=" ")
#     for j in range(num-i,0,-1):
#         print("*",end=" ")
#     print()





# for i in range(num):
#     for j in range(num - i, 1, -1):
#         print("_", end=" ")
#     for j in range(i+1):
#         print("*",end=" ")

#     print()



""" 
_ _ _ @
_ _ # @
_ & # @
$ & # @
       ||||
       ||||
       ||||
       ||||
     \\\\////
      \\\///
       \\//
        \/

"""
ch = ["$","&","#","@","1"]

num = 4

for i in range(1, num+1):
    for j in range(num,i,-1):
        print("_", end=" ")
    for j in range(i,1):
        print(ch[j], end=" ")
    print() 




# ch = ["$","&","#","@"]

# for i in range(4):
#     for j in range(3,i,-1):
#         print("_", end=" ")
#     for j in range( 4-i, 1, -1 ):
#         if i==0:
#             print(ch(len(ch)-i))
#     print()

