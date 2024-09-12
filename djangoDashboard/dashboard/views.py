from django.shortcuts import render
from dashboard.models import Contact
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def contact(request):
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