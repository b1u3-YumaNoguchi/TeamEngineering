from django.urls import path
from django.conf import settings
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login')
]

if settings.DEBUG:
    urlpatterns += [
            path('uitest/', views.uitest, name='uitest'),
            path('logined/', views.logined, name='logined'),
        ]
