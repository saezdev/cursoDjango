from django.urls import re_path, path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    #re_path(r'^$',views.index,name='index'),
    path("", views.IndexView.as_view(), name="index"),
    path('forms/',views.form_name),
    path('users/',views.users),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special'),
    path("registration/", views.register, name='registration'),
    re_path(r'^relative/$',views.relative,name='relative'),
    re_path(r'^others/$',views.other,name='other')
]
