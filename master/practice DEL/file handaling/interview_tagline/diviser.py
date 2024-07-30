# num = input("enter a number : ")
num = 15
multi_set = []
done = []
for i in range(1, num+1):
    single_set = []
    div = num / i  
    div = int(div) 

    if num % div == 0:
        # print(div)
        if div in done:
            pass
        else:
            single_set.append(div)
            other = int(num/div)
            done.append(div)
            done.append(other)
            single_set.append(other)
            multi_set.append(single_set)

print(done)
print(multi_set)



