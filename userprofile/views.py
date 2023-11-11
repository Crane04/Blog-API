from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import *
from rest_framework import status
from django.contrib.auth.models import User, auth
from .models import Token
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import re
from django.contrib.auth.hashers import make_password
from app.models import UserSites
# Create your views here.

class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            token, created = Token.objects.get_or_create(user = user)
            if request.GET.get("next"):
                return redirect(request.GET.get("next"))
            return redirect("/dashboard/admin")
            
        else:
            messages.info(request, "Credentials don't match")
            
            return redirect("/accounts/login")

class SignUpView(View):
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 =request.POST["password2"]

        if password != password2:
            messages.error(request, "Passwords don't match!")
            return redirect("/accounts/signup")
        else:
            if len(password) >= 6 and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[^A-Za-z0-9]', password):

                if User.objects.filter(email = email).exists():
                    messages.error(request, "This email already exists")
                    return redirect("/accounts/signup")
                elif User.objects.filter(username = username).exists():
                    messages.error(request, "User already exists")
                    return redirect("/accounts/login")
                elif User.objects.filter(email = email).exists() == False and User.objects.filter(username = username).exists() == False:
                    hashed_password = make_password(password)
                    user = User.objects.create(username = username, email = email, password= hashed_password)
                    token = Token.objects.create(user = user)
                    user_site = UserSites.objects.create(user = user)
                    user_site.home_page = ""
                    user_site.blog_page = ""
                    user_site.individual_blog_post = ""
                    user.save()
                    token.save()
                    user_site.save()
                    return redirect("/accounts/login")
            else:
                messages.error(request, "Password must contain atleast 6 characters, 1 upper, lowercase and a special character")
                return redirect("/accounts/signup")

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        auth.logout(request)

        return redirect("/accounts/login")
class test_token(APIView):

    def get(self, request:Request, *args, **kwargs):
        return Response({
            
        })