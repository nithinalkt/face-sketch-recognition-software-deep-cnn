from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .forms import StationForm, StationUserForm, CriminalForm, ImageSearchForm
from accounts.models import State, City, Officer, Station, User
from .models import Criminal, ImageSearch
import json, os
from django.conf import settings
from main.single_test import get_criminal

# Create your views here.
def index(request):
    return render(request, 'subadmin/index.html', {})

def add_police_station(request):
    if request.method == 'GET':
        context = {}
        context['form1'] = StationUserForm()
        context['form2'] = StationForm()
        context['states'] = State.objects.all()
        return render(request, 'subadmin/add_police_station.html', context)
    elif request.method == 'POST':
        form1 = StationUserForm(request.POST)
        form2 = StationForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            city = request.POST['city']
            city = City.objects.get(pk=city)
            obj1 = form1.save(commit=False)
            obj2 = form2.save(commit=False)
            obj1.is_station = True
            obj1.set_password(form1.cleaned_data['password'])
            subadmin = Officer.objects.get(user=request.user.id)
            obj2.subadmin = subadmin
            obj2.city = city
            obj1.save()
            obj2.user = obj1
            obj2.save()
            return redirect('subadmin_add_police_station')
        else:
            context = {}
            context['form1'] = form1
            context['form2'] = form2
            context['states'] = State.objects.all()
            return render(request, 'subadmin/add_police_station.html', context)


def get_city(request):
    state = request.GET.get('state')
    district = City.objects.filter(state=state).values()
    data = json.dumps(list(district))
    return JsonResponse({'data': data})

def add_criminals(request):
    if request.method == 'GET':
        context = {}
        context['form1'] = CriminalForm()
        context['states'] = State.objects.all()
        return render(request, 'subadmin/add_criminals.html', context)
    elif request.method == 'POST':
        form1 = CriminalForm(request.POST, request.FILES)
        if form1.is_valid():
            obj = form1.save(commit=False)
            city = City.objects.get(pk=request.POST['city'])
            obj.city = city
            obj.user = request.user
            obj.save()
            return redirect('subadmin_add_criminals')
        else:
            context = {}
            context['form1'] = form1
            context['states'] = State.objects.all()
            return render(request, 'subadmin/add_criminals.html', context)

def search_image(request):
    if request.method == 'GET':
        context = {}
        context['form'] = ImageSearchForm() 
        return render(request, 'subadmin/search_criminal.html', context)
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
            return redirect('subadmin_criminal_details', cid+1)
        else:
            return HttpResponse()

def criminal_details(request, cid):
    context = {}
    try:
        criminal = Criminal.objects.get(person_id=cid)
        context['criminal'] = criminal
    except:
        context['form'] = ImageSearchForm() 
        context['msg'] = 'No criminal found'
        return render(request, 'subadmin/search_criminal.html', context)
    return render(request, 'subadmin/criminal_details.html', context)


def manage_station(request):
    if request.method == 'GET':
        context = {}
        context['data'] = Station.objects.all()
        return render(request, 'subadmin/manage_station.html', context)

def remove_station(request, s_id):
    sub_admin = User.objects.get(id=s_id)
    sub_admin.delete()
    return redirect('subadmin_manage_station')


def manage_criminals(request):
    if request.method == 'GET':
        context = {}
        context['data'] = Criminal.objects.all()
        return render(request, 'subadmin/manage_criminals.html', context)

def remove_criminals(request, cid):
    sub_admin = Criminal.objects.get(id=cid)
    sub_admin.delete()
    return redirect('subadmin_manage_criminals')

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
            return redirect('subadmin_add_criminals')
        else:
            context = {}
            context['form1'] = form1
            context['states'] = State.objects.all()
            return render(request, 'subadmin/add_criminals.html', context)