from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from home.models import Contacts, Subscribe
# Create your views here.

def index(request):
    if request.method == "POST":
        email = request.POST.get('email')
        subscribe = Subscribe(email=email, date=datetime.today())
        subscribe.save()
        messages.success(request, 'Thank You for Subscribing')
    return render(request, 'index.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logges In")
            return redirect("/")
        else:
            messages.success(request, "Bad Credentials!")
            return redirect('signin')
    else:
        return render(request, 'signin.html')

def signup(request):
    try:
        if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname

            user.save()
            messages.success(request, "Your account has been successfully created.")

            return redirect('/')
    except:
        messages.error(request, "Enter a valid username!!")
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect('/')

def about(request):
    return render(request, 'about.html')

def offers(request):
    return render (request, 'offers.html')

def purchase(request):
    return render (request, 'purchase.html')
    
def contacts(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        desc =request.POST.get('desc')
        
        contacts = Contacts(name=name, email=email, phone=phone, desc=desc, date =datetime.today())
        contacts.save()
        
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contacts.html')
    
