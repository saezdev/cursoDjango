from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from . import forms
from first_app.forms import NewUserForm, UserProfileInfoForm, UserForm
from django.views.generic import View

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

class CBView(View):
    def get(self,request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!")

""" def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list, 'text':'Hello World', 'number':'100'}
    my_dic = {'insert_me':"Hello i am from first_app/index.html!"}
    return render(request, 'first_app/index.html', context=date_dict) """

def form_name(request):
    form = forms.FormName()
    
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        
        if form.is_valid():
            #DO SOMETHING HERE
            print('VALIDATION SUCCESS!')
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])
            
    return render(request, 'first_app/forms.html', {'form': form})

def users(request):
    form = NewUserForm()
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID!")
            
    return render(request, 'first_app/users.html', {'form': form})

def other(request):
    return render(request,'first_app/other.html')

def relative(request):
    return render(request, 'first_app/relative_url_templates.html')

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
                profile.profile_pic = request.FILES['profile_pic']
        
            profile.save()
            registered = True
            
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/registration.html',{
        'user_form':user_form,
        'profile_form':profile_form,
        'registered':registered,
    })
    
#This decorator makes the view require a person to be logged in in order to see it
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("YOU ARE LOGGED IN, NICE!")
    
    
def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username = username, password = password)
        
        if user:
            if user.is_active:
                login(request,user)
                #If they login and its successful and their account is active it will reverse them and redirect back to the index page.
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
            
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password: {} ".format(username,password))
            return HttpResponse("INVALID LOGIN DETAILS SUPPLIED")
    else:
        return render(request,'first_app/login.html')    
                

        
           