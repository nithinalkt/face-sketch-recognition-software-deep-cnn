from django.shortcuts import render, redirect
from subadmin.models import ImageSearch, Criminal
from subadmin.forms import ImageSearchForm
from django.conf import settings
from main.single_test import get_criminal
from subadmin.forms import CriminalForm
from accounts.models import State, City

# Create your views here.


def index(request):
    if request.method == 'GET':
        context = {}
        context['form'] = ImageSearchForm() 
        return render(request, 'station/index.html', context)
    elif request.method == 'POST':
        form = ImageSearchForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                obj = ImageSearch.objects.get(user=request.user.id)
                obj.image = request.FILES['image']
                obj.save()
            except:
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
            filename = str(obj.image)
            filename = filename.split('/')
            path=settings.BASE_DIR+"\\media\\Temp\\"+str(filename[1])
            print(path)
            cid = get_criminal(path)
            return redirect('station_criminal_details', cid+1)

def add_criminals(request):
    if request.method == 'GET':
        context = {}
        context['form1'] = CriminalForm()
        context['states'] = State.objects.all()
        return render(request, 'station/add_criminals.html', context)
    elif request.method == 'POST':
        form1 = CriminalForm(request.POST, request.FILES)
        if form1.is_valid():
            obj = form1.save(commit=False)
            city = City.objects.get(pk=request.POST['city'])
            obj.city = city
            obj.user = request.user
            obj.save()
            return redirect('station_add_criminals')
        else:
            context = {}
            context['form1'] = form1
            context['states'] = State.objects.all()
            return render(request, 'station/add_criminals.html', context)

def manage_criminals(request):
    if request.method == 'GET':
        context = {}
        context['data'] = Criminal.objects.filter(user=request.user.id)
        return render(request, 'station/manage_criminals.html', context)

def remove_criminals(request, cid):
    sub_admin = Criminal.objects.get(id=cid)
    sub_admin.delete()
    return redirect('station_manage_criminals')

def edit_criminals(request,cid):
    criminal = Criminal.objects.get(pk=cid)
    if request.method == 'GET':
        context = {}
        context['form1'] = CriminalForm(instance=criminal)
        context['states'] = State.objects.all()
        return render(request, 'subadmin/add_criminals.html', context)
    elif request.method == 'POST':
        form1 = CriminalForm(data=request.POST, files=request.FILES, instance=criminal)
        if form1.is_valid():
            obj = form1.save(commit=False)
            city = City.objects.get(pk=request.POST['city'])
            obj.city = city
            obj.save()
            return redirect('station_add_criminals')
        else:
            context = {}
            context['form1'] = form1
            context['states'] = State.objects.all()
            return render(request, 'station/add_criminals.html', context)


def criminal_details(request, cid):
    context = {}
    try:
        criminal = Criminal.objects.get(person_id=cid)
        context['criminal'] = criminal
    except:
        context['form'] = ImageSearchForm() 
        context['msg'] = 'No criminal found'
        return render(request, 'station/index.html', context)
    return render(request, 'station/criminal_details.html', context)