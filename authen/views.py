from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
import re
from .models import ProfilePic


def valid_pass(pasw):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
    return re.match(pattern, pasw)


def register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pasw = request.POST['pasw']
        cpasw = request.POST['con_pasw']

        try:
            User.objects.get(username=uname)
            messages.error(request, 'Username already exists..!')
            return redirect('register')

        except User.DoesNotExist:

            if pasw != cpasw:
                messages.error(
                    request,
                    'Password and confirm password are not matching..!'
                )
                return redirect('register')

            if not valid_pass(pasw):
                messages.error(
                    request,
                    'Password should be minimum 8 characters and contain uppercase, lowercase, number and special character.'
                )
                return redirect('register')

            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']

            u = User.objects.create(
                first_name=fname,
                last_name=lname,
                username=uname,
                email=email,
            )

            u.set_password(pasw)
            u.save()

            messages.success(request, 'Registered successfully..!')
            return redirect('login_')
    return render(request, 'register.html')

def login_(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pasw = request.POST['pasw']
        user = authenticate(username=uname,password=pasw)
        if user:
            login(request,user)
            messages.success(request,'login successfull....!')
            return redirect('home')
        else:
            messages.error(request,'entered username or password is incorrect..!')
            return redirect('login_')
    return render(request,'login_.html')

def logout_(request):
    logout(request)
    messages.success(request,'logged out successfull.....!')
    return redirect('login_')

def profile(request):
        profile=ProfilePic.objects.get(user=request.user)
        return render(request,'profile.html',{'profile':profile})


def respasw(request):
    if request.method == 'POST':
        if 'opasw' in request.POST:
            old_pass = request.POST['opasw']
            user = authenticate(username=request.user.username, password=old_pass)
            if user:
                messages.success(request, 'Enter new Password..!')
                return render(request, 'respasw.html', {'new': True})
            else:
                messages.error(request, 'Entered password is incorrect..!')
                return redirect('respasw')
        if 'npasw' in request.POST and 'c_pasw' in request.POST:
            new_pass = request.POST['npasw']
            confirm_pass = request.POST['c_pasw']
            user = User.objects.get(username=request.user.username)

            if new_pass != confirm_pass:
                messages.error(request, 'New and confirm password do not match!')
                return redirect('respasw')

            user.set_password(new_pass)
            user.save()
            messages.success(request, 'Password updated successfully!')
            return redirect('login_')

    return render(request, 'respasw.html')

def update_pro(request):
    profile = ProfilePic.objects.get(user = request.user)
    if request.method == 'POST':
        user = User.objects.get(username = user)
        a = request.POST['fname']
        b= request.POST['lname']
        c = request.POST['uname']
        d = request.POST['email']
        user = request.user
        user.first_name = a
        user.last_name = b
        user.username = c
        user.email = d
        user.save()
        messages.success(request,'profile updated successfull....!')
        return redirect('profile')
    return render(request,'update_pro.html')


def forget_pasw(request):
    if request.method == 'POST':
        if 'uname' in request.POST:
            uname = request.POST['uname']
            try:
                a = User.objects.get(username=uname)
                request.session['fp_user'] = a.username
                messages.success(request,'enter new password..!')
                return render(request,'forget_pasw.html',{'new':True, 'old':a})
            except:
                messages.error(request,'username doesnt match...!')
                return redirect('forget_pasw')
            
        if 'newp' in request.POST:
            b = request.POST['newp']
            c = request.POST['conf_pasw']
            user = request.session.get('fp_user')
            data = User.objects.get(username=user)

            if b != c:
                messages.error(request,'entered paswwords doesnt match..!')
                return redirect('forget_pasw')
            if data.check_password(b):
                messages.error(request,'password already exists..!')
                return redirect('forget_pasw')
            
            data.set_password(b)
            data.save()
            messages.success(request,'Password updated successfully...!')
            return redirect('login_')
    return render(request,'forget_pasw.html')