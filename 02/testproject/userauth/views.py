from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib import messages
from userauth.forms import register_form
from userauth.forms import login_form
from django.contrib import messages
from django.shortcuts import redirect

def register_view(request):
    form = register_form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('login')
    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = login_form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username,password=password)
        if user:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid username or password.')
    return render(request,'login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request,"You have been logged out.")
        return redirect('pageone')
    else:
        return render(request, 'pageone.html',{'user':request.user})