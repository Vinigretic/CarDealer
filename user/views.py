from django.shortcuts import render



def login(request):
    return render(request, 'user/login.html')

def logout(request):
    return render(request, 'user/logout.html')

def user(request):
    return render(request, 'user/user.html')

def registration(request):
    return render(request, 'user/registration.html')




