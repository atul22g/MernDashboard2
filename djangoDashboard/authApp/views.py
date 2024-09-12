from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def Signin(request):
    if request.method == "POST":
        usenName = request.POST.get('usenName')
        password = request.POST.get('password')
        user = authenticate(username=usenName, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully.")
            return redirect('dashboard')
        else:
            messages.warning(request, "The username or password is incorrect.")
    return render(request, 'Signin.html')

def Signup(request):
    if request.method == "POST":
        usenName = request.POST.get('usenName')
        password = request.POST.get('password')
        Cpassword = request.POST.get('Cpassword')
        if password != Cpassword:
            messages.warning(request, "The Password does not match!")
        else:
            try:
                user = User.objects.create_user(username=usenName, password=password)
                user.save()
                messages.success(request, "User has been created successfully.")
            except:
                messages.warning(request, "User is not created.")
    return render(request, 'Signup.html',{'message': 'Password does not match!'})