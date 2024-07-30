# with open("example.txt","r") as file:
#     print(file.read())


text = ['i am imroz khan and i am here for learning\n', 'i am imroz khan and i am here for learning\n', 'i am imroz khan and i am here for learning\n', 'i am imroz khan and i am here for learning\n', 'i am imroz khan and i am here for learning\n', 'i am imroz khan and i am here for learning\n', 'i am imroz khan and i am here for learning\n', 'i am imroz khan and i am here for learning\n', 'i am imroz khan and i am here for learning\n', 'i am imroz khan and i am here for learning']


# with open("example2.txt","a") as file:
#     for i in text:
#         file.write(i)
#     file.close()


file = open("hello_world.txt", "a")
for i in text:
    file.write(i)
file.close()
 