set_items = { 1, 2 ,3,4,5,6,7,8,9 }


# set_list = dir(set_items)

# set_method = []

# for i in set_list :
#     if i.startswith("__") :
#         pass
#     else:
#         set_method.append(i)

# # print(set_method)

# for ind , i in enumerate(set_method) :
#     print(f"{ind+1} : {i}")

dict_method = """
1 : add
2 : clear
3 : copy
4 : difference
5 : difference_update
6 : discard
7 : intersection
8 : intersection_update
9 : isdisjoint
10 : issubset
11 : issuperset
12 : pop
13 : remove
14 : symmetric_difference
15 : symmetric_difference_update
16 : union
17 : update
"""
# print(dict_method)
new_list = dict_method.split()

for i in new_list:
    # print(i)
    if i.isdigit():
        pass


# print(new_list)


# new_s= " ".join(new_list)
# print(new_s)




# print


# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set1.difference_update(set2)
# print(set1)  # Output: {1, 2}

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
diff = set1.difference(set2)
# print(diff)  # Output: {1, 2}


# # Creating a set
my_set = {1, 2, 3, 4, 5}

# # Adding elements to a set
# my_set.add(6)
# print(my_set)

# # Removing elements from a set
# my_set.remove(3)
# print(my_set)

# # Union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # Output: {1, 2, 3, 4, 5}

# print(union_set)

# # Intersection of sets
intersection_set = set1.intersection(set2)  # Output: {3}

""" 
# Define two sets
set1 = {1, 2, 3, 4, 5,7}
set2 = {3, 4, 5, 6, 7}

# Find the intersection of sets
intersection_set = set1.intersection(set2)

# Print the intersection set
print("Intersection Set:", intersection_set)
"""

# # Difference of sets
difference_set = set1.difference(set2)  # Output: {1, 2}




""" 
# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Find the difference between set1 and set2
difference_set = set1.difference(set2)

# Print the difference set
print("Difference Set (set1 - set2):", difference_set)
"""




# # Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)  # Output: {1, 2, 4, 5}

# # Checking subset
# is_subset = set1.issubset(set2)  # Output: False

# # Checking superset
# is_superset = set1.issuperset(set2)  # Output: False

# # Checking disjoint sets
# is_disjoint = set1.isdisjoint(set2)  # Output: False

