# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = input("enter : ")

# if f"{x}" in thisdict:
#   print(f"Yes, '{x}' is one of the keys in the thisdict dictionary. and the value is {thisdict[x]}.")
# else:
#   print(f"{x} is not a key in dictionary")



myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#print(myfamily)

for x,y in myfamily.items():
    # print(x)
    # print(type(x))
    # print(type(y))

    for i,j in y.items():
        print(j)
    print()