from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import login
from django.contrib.auth import logout


def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)  #
        if form.is_valid():
            formdata = form.cleaned_data  # erase whatever there was there
            username = formdata['Username']
            password = formdata['Password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home')
            else:
                return render(request, 'authentication/login.html', {'form': form, 'failure': True})

    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form, 'failure': False})


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
