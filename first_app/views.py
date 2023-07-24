from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from . import forms

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
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