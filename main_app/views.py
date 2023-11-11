from django.shortcuts import render, redirect

from app_forms import StudentForm
from main_app.models import Student


# Create your views here.
def students(request):
    if request.method == 'POST':
        # the script to check if the form is valid and all field are ok
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # redirect function .please import fom django shortcuts
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'students.html', {'form': form})


def show_students(request):
    data = Student.objects.all()
    return render(request, 'display.html', {'students': data})


def details(request, id):
    student = Student.objects.get(pk=id) #SELECT* FROM  students where
    return render(request, 'details.html', {'student': student})
