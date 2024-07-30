def even_odd(num):
    try:
        while True:
            try:
                if num == True:
                    pass
                else:
                    num = int(input("enter a number : "))
                if num % 2 == 0:
                    print("even")
                else:
                    print("odd")
            except ValueError:
                print("Something went wrong : invalid literal for int() with base 10")
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")

try:
    even_odd(0)
except Exception as e :
    print(e)