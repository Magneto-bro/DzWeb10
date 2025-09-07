from django.shortcuts import render ,redirect
from django.contrib.auth import login,logout,authenticate 
from django.contrib.auth.forms import AuthenticationForm
from .forms import  SignUpForm
from django.contrib import messages
# Create your views here.

def signup_view(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Реєстрація пройшла успішно")
            return redirect('quotes:all_quotes')
    else:
        form =SignUpForm()
    return render(request,'accounts/signup.html',{'form': form})


def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,'Вхід успішний')
            return redirect('quotes:all_quotes')
    else:
        form =AuthenticationForm()

    return render(request,"accounts/login.html",{"form":form})

def logout_view(request):
    logout(request)
    messages.info(request,'Ви вийшли з акаунту')
    return redirect('login')