from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

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
    student = Student.objects.get(pk=id)  # SELECT* FROM  students where
    return render(request, 'details.html', {'student': student})


# def delete_student(request, student_id):
#     student = get_object_or_404(Student, pk=student_id)
#     student.delete()
#     return redirect('show')


def students_search(request):
    search = request.GET['search']
    data = Student.objects.filter(
        Q(first_name__icontains=search)
        | Q(last_name__icontains=search)
        | Q(email__icontains=search)
    )

    if search.isnumeric():
        score = int(search)
        data = Student.objects.filter(kcpe_score=score)
    return render(request, 'display.html', {'students': data})

# elastic search
