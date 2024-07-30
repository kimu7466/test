from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.method == "POST":
        user_ = request.POST["user"]
        password_ = request.POST["password"]

        print(user_)
        print(password_)
        
        
        pass
    return render(request, "login.html")
