
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .forms import contact_usform, loginform
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login

def home(request):
    return render(request, 'main/home.html')


def colleges(request):
    return render(request, 'main/colleges.html')
    

def students(request):
    students_data = [
        {'name': 'Anu', 'branch': 'IT', 'age': 19},
        {'name': 'Raju', 'branch': 'CSE', 'age': 17},
        {'name': 'Kiran', 'branch': 'ECE', 'age': 20},
    ]
    return render(request, 'main/students.html', {'students': students_data})

def login(request):
    form=loginform(request.POST or None)
    return render(request, 'main/login.html', {'form': form})


def loginverification(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        password=request.POST.get('password')   
        if uname=="":
            print("sorry")
            return HttpResponse("sorry")
        else:
            user=authenticate(request, username=uname, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponse("welcome")
            else:
                request.session['username'] = uname
                return redirect("login")
            return HttpResponse(uname)


def address(request):
    return render(request, 'main/address.html')

def contact_us(request):
    form = contact_usform(request.POST or None)
    if form.is_valid():
        send_mail(
            form.cleaned_data['subject'],
            form.cleaned_data['message'],
            settings.EMAIL_HOST_USER,
            [form.cleaned_data['to_email']]
        )
        return render(request, 'main/contact_us.html', {'form': form, 'success': True})
    return render(request, 'main/contact_us.html', {'form': form})
   
# Create your views here.
