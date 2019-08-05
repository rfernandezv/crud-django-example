from django.shortcuts import render
from seguridad.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('seguridad:login'))
        #return render(request, 'seguridad/login.html', {})
    return render(request,'seguridad/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'seguridad/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):    
    username = ""
    password = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')        

        _resultValidation, _context = login_validation(username, password)
        if not _resultValidation:
            return render(request, 'seguridad/login.html', _context)        

        user = authenticate(username=username, password=password)        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'seguridad/login.html', {"username":username})

def login_validation(username, password):
    if not username:
        return False,{"error":"Por favor ingrese el usuario","username":username}
    if not password:
        return False,{"error":"Por favor ingrese la contraseña","username":username}
    return True,{}