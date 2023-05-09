from django.shortcuts import render, redirect
from .models import Room
from .models import Product
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home(request):
    room = Room.objects.all()
    product = Product.objects.all()
    context = {'room':room, 'product':product}
    return render(request, 'app/home.html', context)

def room(request):
    room = Room.objects.all()
    # messages = room.message_set.all()
    context = {'room':room}
    return render(request, 'app/room.html',context )

def about(request):
    return render(request, 'app/about.html')

def events(request):
    return render(request, 'app/events.html')

def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context ={'form' : form}
    return render(request, 'app/room_og.html', context)

def updateRoom(request,pk):
    product = Product.objects.get(id=pk)
    form = RoomForm(instance=product)
    if request.method == "POST":
        form = RoomForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'app/room_og.html', context)

def deleteRoom(request,pk):
    roomdelete = Product.objects.get(id=pk)
    if request.method == "POST":
        roomdelete.delete()
    return render(request,'app/delete.html', {'obj':room})

def services(request):
    context = {}
    return render(request,'app/services.html', context)

def contact(request):
    return render(request,'app/contact.html')

@login_required(login_url='loginPage')
def excreate(request):
    exform = RoomForm()
    if request.method == "POST":
        exform = RoomForm(request.POST)
        if exform.is_valid():
            exform.save()
            redirect('home')
    context = {'exform':exform}
    return render(request, 'app/excreate.html', context)

def exupdate(request, pk):
    product = Product.objects.get(id=pk)
    product = RoomForm(instance=product)
    if request.method == "POST":
        product = RoomForm(request.POST,instance=product)
        if product.is_valid():
            product.save()
    context = {'product': product}
    return render(request, 'app/excreate.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def loginPage(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')


        try:
            user = User.object.get(username=username)
        except:
            messages.error(request, 'User doesnt exist')


        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, 'Username and password does not exist')

    
    context = {'page': page }
    return render(request, 'app/login_register.html', context)

def registerPage(request):
    page = 'register'
    form = UserCreationForm()

    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, ' An error occured during registration ')
    return render(request,'app/login_register.html', {'form':form})


def poland(request):
    context = {}
    return render(request,'app/poland.html', context)

def loginNow(request):
    if request.method == 'POST':
        username = username.POST.get('username')
        password = password.POST.get('password')
        try:
            user = User.objects.get('username')
        except:
            messages.error(request,'Username is not exist')
        
        user = authenticate(request, usename=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")            
        else:
            messages.error(request,"username and password does not exist")
    context = {}
    return render(request,'app/login_now.html', context)

def registerNow(request):
    if request.method == 'POST':
        formone = UserCreationForm()
        if formone.is_valid():
            user = formone.save(commit=False)
            user.username = user.username.lower()
            login(request, user)
    return render(request, 'app/login_now.html', request)

def gallery(request): 
    context = {}
    return render(request, 'app/gallery.html', context)

def roomtwo(request):
    roomtwo = Room.objects.all()
    context ={'roomtwo':roomtwo}
    return render(request,'app/roomtwo.html', context)


def loginweek(request):
    if request.method == "POST":
        username = username.POST.get('username')
        password = password.POST.get('password')
        try:
            user = User.objects.get('username')
        except:
            messages.error(request, 'username does not exist')
        user = authenticate(request, uxsername=username, password=password)
        if user is not None:
            login(request, user)
            return render('home')
        else:
            messages.error(request, "username and password not match")
    context = {}
    return render(request, 'app/loginweek.html', context)

def login(request):
    if request.method == "POST":
        username = username.POST.get('username')
        password = password.POST.get('password')
        try:
            user = User.objects.get('username')
        except:
            messages.error(request, 'username does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, 'username and password not match')
    context = {}
    return render(request,  "app/login_now.html",context)

def usa(request):
    context = {}
    return render(request, "app/usa.html", context)


def canada(request):
    context ={}
    return render(request,'app/canada.html', context)

def otherUniversity(request):
    context = {}
    return render(request, 'app/otherUniversity.html', context)

