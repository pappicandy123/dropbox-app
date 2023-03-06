from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'index.html')




def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Signup Successful')
            return redirect('index')
        else:
            form = SignupForm()
    return render(request, 'signup.html', {'form':form})




# def login(request):
#     if request.method =="POST":
#         name = request.POST['username']
#         passw = request.POST['password']
#         user = authenticate(username = name, password = passw)
#         if user:
#             login(request, user)
#             messages.success(request, 'signin successful')
#             return redirect('index')
#         else:
#             messages.warning(request, 'username/password incorrect')
#             return redirect('login')
#     return render(request, 'login.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request, 'signin successful')
            return redirect('index')
        else:
            messages.warning(request, 'username/password incorrect')
            return redirect('login')
    return render(request, 'login.html')


def signout(request):
    logout(request)
    return redirect('login')