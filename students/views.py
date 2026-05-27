from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def admission(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            course=request.POST['course'],
            address=request.POST['address'],
        )
        messages.success(request, 'Admission submitted successfully!')
        return redirect('admission')

    return render(request, 'admission.html')

    

def fees(request):
    return render(request, 'fees.html')

def placement(request):
    return render(request, 'placement.html')

def contact(request):
    return render(request, 'contact.html')
