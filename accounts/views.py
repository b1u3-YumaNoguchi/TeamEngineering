from django.shortcuts import render
from django.contrib.auth import views
from django.http import HttpResponse


def uitest(req):
    return render(req, 'accounts/login.html', {'page_title': 'Login'})


def logined(req):
    return HttpResponse(f'logined as {req.user.username}')


class LoginView(views.LoginView):
    template_name = 'accounts/login.html'

