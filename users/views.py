from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddForm, userAuth
from django.contrib.auth.decorators import login_required
import hashlib, random, string
from .models import User
from django.core.mail import send_mail
from django.contrib import auth


class Home:
    def index(request):
        request = request
        users = User.objects.all()
        return render(request, 'users/index.html', {'users': users})


class utils:
    def pass_hash(unhashed):
        hashed = hashlib.sha256(unhashed)
        hashed = hashed.hexdigest()
        return hashed

    def random_pass(self):
        return ''.join(random.choice(string.ascii_letters) for i in range(32))


class AddUser:
    @login_required(login_url='/users/login/')
    def add_user(request):
        form = AddForm(request.POST or None)
        if form.is_valid():
            obj = utils()
            data = form.save(commit=False)
            unhashed = obj.random_pass()
            send_mail('Login Password', unhashed, 'Django-admin', [data.email])
            hashed = obj.pass_hash(unhashed.encode())
            data.password = hashed
            print(hashed)
            data.save()
            return redirect('/users/')

        return render(request, 'users/add_user.html', {'form': form})


class Auth:
    def user_login(request):
        form = userAuth(request.POST or None)
        if form.is_valid():
            auth_data = form.cleaned_data
            try:
                user = User.objects.get(pk=auth_data['username'])
            except:

                return redirect('/users/login/')

            saved_password = user.password
            saved_email = user.email
            if (saved_email == auth_data['username'] and saved_password == utils.pass_hash(
                    auth_data['password'].encode())):

                return redirect('/users/')

            else:
                redirect('/')


        return render(request, 'users/user_login.html', {'form': form})

    def logout(self,request):
        self.request = request
        auth.logout(self.request)
        return redirect('/users/login/')
