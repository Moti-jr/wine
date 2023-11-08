from django.shortcuts import render

from app_forms import StudentForm


# Create your views here.
def students(request):
    form = StudentForm()

    return render(request, 'students.html',{'form':form})
