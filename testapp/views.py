from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import AccessRecords, Topic, Webpage
from testapp.forms import FormName

# Create your views here.
def index(request):
    my_dict = {'Manufacturer': "Lamborghini", 'Model': "Hurracan"}
    return render(request, 'index.html', context=my_dict)


def alldata(request):
    my_records = AccessRecords.objects.order_by('date')
    data_dict = {'all_records': my_records}
    return render(request, 'data.html', context=data_dict)


def allwebdata(request):
    all_web_records = Webpage.objects.order_by('name')
    web_dict = {'all_records': all_web_records}
    return render(request, 'webdata.html', context=web_dict)


def myformview(request):
    forms = FormName()

    if request.method == 'POST':
        submitted_form = FormName(request.POST)

        if submitted_form.is_valid():
            print('Name: ' + submitted_form.cleaned_data['name'])
            print('Email: ' + submitted_form.cleaned_data['email'])
            print('Text: ' + submitted_form.cleaned_data['text'])


    return render(request, 'myform.html', {'form': forms})
