from django.shortcuts import render
from dashboard.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        date = datetime.now()
        try:
            contactData = Contact(name=name, email=email, message=message, date=date)
            contactData.save() # Save the data to the database
            messages.success(request, "Your message has been sent successfully.")
        except:
            messages.warning(request, "Your message is not sent.")
            
    return render(request, 'contact.html')