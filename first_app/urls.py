from django.urls import re_path, path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    path('forms/',views.form_name),
    path('users/',views.users),
    re_path(r'^relative/$',views.relative,name='relative'),
    re_path(r'^others/$',views.other,name='other')
]
