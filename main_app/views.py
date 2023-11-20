from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from app_forms import StudentForm
from main_app.app_forms import LoginForm
from main_app.models import Student


# Create your views here.
@login_required  # decorators
def students(request):
    if request.method == 'POST':
        # the script to check if the form is valid and all field are ok
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'user saved successfully')
            messages.error(request, 'error while saving data')
            messages.error(request, 'this action is fatal')
            messages.info(request, 'kesho ni weekend')
            # redirect function .please import fom django shortcuts
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'students.html', {'form': form})


@login_required  # decorators
def show_students(request):
    data = Student.objects.all()

    paginator = Paginator(data, 50)
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    return render(request, 'display.html', {'students': data})
    # return render(request, 'details.html', {'student': student})


@login_required  # decorators
def details(request, id):
    student = Student.objects.get(pk=id)  # SELECT* FROM  students where
    return render(request, 'details.html', {'student': student})


@login_required  # decorators
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return redirect('show')


@login_required
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
        paginator = Paginator(data, 50)
        page_number = request.GET.get('page')
        data = paginator.get_page(page_number)
        return render(request, 'display.html', {'students': data})
    # return render(request, 'display.html', {'students': data})


# elastic search
@login_required
def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)  # select*FROM students where id=1
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)  # it does the comparison and save the file
        if form.is_valid():
            messages.success(request, f'successfully updated {student.first_name}')
            form.save()

        return redirect('details', student_id)
    else:
        form = StudentForm(instance=student)

    return render(request, 'update.html', {'form': form})


def signin(request):
    if request.method == 'GET':

        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'signed in successfully')
                return redirect('home')
        messages.error(request, 'invalid username or password')
        return render(request, 'login.html', {'form': form})


def signout(request):
    logout(request)  # kill al the cookies and sessions
    return redirect('login')
