from django.shortcuts import render, redirect

from app_forms import StudentForm


# Create your views here.
def students(request):
    if request.method == 'POST':
        # the script to check if the form is valid and all field are ok
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect function .please import fom django shortcuts
            return redirect('home')

    form = StudentForm()
    return render(request, 'students.html', {'form': form})

