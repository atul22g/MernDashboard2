from django.shortcuts import render, redirect
from dashboard.models import Contact
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'dashboard.html')

def contact(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        try:
            contactData = Contact(name=name, email=email, message=message)
            contactData.save() # Save the data to the database
            messages.success(request, "Your message has been sent successfully.")
        except:
            messages.warning(request, "Your message is not sent.")
            
    return render(request, 'contact.html')

def logout_view(request):
    logout(request)
    return redirect('/')