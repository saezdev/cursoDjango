from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from . import forms
from first_app.forms import NewUserForm, UserProfileInfoForm, UserForm

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list, 'text':'Hello World', 'number':'100'}
    my_dic = {'insert_me':"Hello i am from first_app/index.html!"}
    return render(request, 'first_app/index.html', context=date_dict)

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
        
        
        