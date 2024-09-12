from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def Signin(request):
    return render(request, 'Signin.html')

def Signup(request):
    if request.method == "POST":
        usenName = request.POST.get('usenName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        Cpassword = request.POST.get('Cpassword')
        if password != Cpassword:
            messages.warning(request, "The Password does not match!")
        else:
            try:
                user = User.objects.create_user(username=usenName, email=email, password=password)
                user.save()
                messages.success(request, "User has been created successfully.")
            except:
                messages.warning(request, "User is not created.")

        # contactData = Contact(name=name, email=email, message=message)
        # contactData.save() 
    return render(request, 'Signup.html',{'message': 'Password does not match!'})