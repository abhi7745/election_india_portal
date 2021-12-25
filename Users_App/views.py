from django.contrib import admin
from django.shortcuts import render,redirect

# importing all app models
from Users_App.models import *

# importing password encryptor
from django.contrib.auth.hashers import make_password, check_password

# importing django login athentications
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    
    return render(request,'index.html',{})

def signup(request):
    if request.user.is_authenticated:
        print('User Already logined')
        return redirect(index)
    
    else:
        if request.method=='POST':
            email=request.POST.get('s_email')
            password=request.POST.get('s_psd')
            confirm_psd=request.POST.get('confirm_psd')
            print(email)
            print(password)
            print(confirm_psd)

            if(email== '' or password==''):
                    print('No value')
                    return render(request,'signup.html',{'checker':'Please enter valid info...!','static_mail':email})

            elif(not password==confirm_psd):
                print('Password Missmatch')
                return render(request,'signup.html',{'checker':'Password Missmatch...!','static_mail':email})
                    
            elif(not email.endswith('@gmail.com')):
                print('Invalid Email...!')
                return render(request,'signup.html',{'checker':'Invalid Email...!','static_mail':email})
                    
            elif User.objects.filter(username=email).exists():
                print('User already exist')
                return render(request,'signup.html',{'checker':'User already exist..!.','static_mail':email})

            else:
                #making password encryption for login purpose(becz django weak password is not allowed in authentication)
                passEncrypted = make_password(password)

                # creating User table object
                auth_user=User()
                auth_user.username=email.lower()# lower() is for converting email uppercase letter to lower case letter
                auth_user.password=passEncrypted
                auth_user.first_name='wardmanager'
                auth_user.save()
                print("Signup successful")

                return render(request,'login.html',{'checker':'Account Created Successfully.. Please Login..!'})

    
    return render(request,'signup.html',{})

def loginpage(request):
    if request.user.is_authenticated:
        print('User Already logined')
        return redirect(index)
    
    else:
        if request.method=='POST':
            email=request.POST.get('email')
            password=request.POST.get('password')
            print(email)
            print(password)

            if(email== '' or password==''):
                print('No value')
                return render(request,'login.html',{'checker':'Please enter valid info...!','static_mail':email})

            elif(not email.endswith('@gmail.com')):
                print('Invalid Email...!')
                return render(request,'login.html',{'checker':'Invalid Email...!','static_mail':email})
                
            else:
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                    print('user login success')

                        
                    return redirect(index)

                else:
                    return render(request,'login.html',{'checker':'Invalid Username or Password','static_mail':email})
    
    return render(request,'login.html',{})


# admin logic area
def admin_dashboard(request):
    return render(request,'admin/dashboard.html',{})

# ////////////////////////////////////////////////////////////////////////
# Ward_manager logic area
# dashboard
def ward_manager(request):
    return render(request,'ward_manager/dashboard.html',{})

# ward_manager_profile
def ward_man_profile(request):
    return render(request,'ward_manager/ward_man_profile.html',{})

# election_setter
def election_setter(request):
    return render(request,'ward_manager/election_setter.html',{})

# add_booth_member page
def add_booth_member(request):
    return render(request,'ward_manager/add_boothmemb.html',{})


# //////////////////////////////////////////////////////////////////////////
# booth_member logic area
def booth_member(request):
    return render(request,'booth_member/dashboard.html',{})