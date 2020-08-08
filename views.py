from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages
from .forms import  CreateUserForm



def registerpage(request):
    form= CreateUserForm()

    if request.method == 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            return redirect('login')

    context = {'form': form}
    return render ( request, 'register.html', context)


def loginpage(request):
    context = {}
    return render (request, 'login.html' , context)
