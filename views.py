from django.shortcuts import render, redirect
from .forms import CaseTypeForm, CaseType
from accounts.forms import UserForm, OfficerForm
from accounts.models import Officer, User

# Create your views here.
def index(request):
    return render(request, 'admin/index.html')

def add_case_type(request):
    if request.method == 'GET':
        context = {}
        context['form'] = CaseTypeForm()
        context['case_types'] = CaseType.objects.all()
        return render(request, 'admin/add_case_type.html', context)
    elif request.method == 'POST':
        form = CaseTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_case_type')
        else:
            return render(request, 'admin/add_case_type.html', {'form': form})

def remove_case_type(request, case_type_id):
    case_type = CaseType.objects.get(id=case_type_id)
    case_type.delete()
    return redirect('add_case_type')

def add_sub_admin(request):
    if request.method == 'GET':
        context = {}
        context['form1'] = UserForm()
        context['form2'] = OfficerForm()
        return render(request, 'admin/add_sub_admin.html', context)
    elif request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = OfficerForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            obj = form1.save(commit=False)
            obj.set_password(form1.cleaned_data['password'])
            obj.is_staff=True
            obj.save()
            officer = form2.save(commit=False)
            officer.user = obj
            officer.save()
            return redirect('add_sub_admin')
        else:
            context = {}
            context['form1'] = form1
            context['form2'] = form2
            return render(request, 'admin/add_sub_admin.html', context)

def manage_sub_admins(request):
    context = {}
    context['users'] = Officer.objects.all()
    return render(request, 'admin/manage_sub_admins.html', context)

def remove_sub_admin(request, sub_id):
    sub_admin = User.objects.get(id=sub_id)
    sub_admin.delete()
    return redirect('manage_sub_admins')