from django.shortcuts import render,redirect
from .models import Patient
from .forms import PatientForm

# Create your views here.

def insert_view(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'star/new.html',{'form':form})

def show_view(request):
    patients = Patient.objects.all()
    return render(request,'star/allpatient.html',{'patients':patients})

def delete_view(request,id):
    patients = Patient.objects.get(id = id)
    patients.delete()
    return redirect('/show')   

def update_view(request,id):
    patients = Patient.objects.get(id = id)
    form = PatientForm(request.POST,instance=patients)
    if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    return render(request,'star/update.html',{'patients':patients})

