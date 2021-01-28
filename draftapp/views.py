from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import CreateStudentForm
from .forms import CreateTeacherForm
from .models import Student
from .models import Teacher
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def reghome(request):
    return render(request, 'draftapp/reghome.html')


@login_required
def adds(request):
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/registration/views')
    else:
        form = CreateStudentForm()
    return render(request, 'draftapp/createstudent.html', {'form': form})


@login_required
def addt(request):
    if request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/registration/viewt')
    else:
        form = CreateTeacherForm()
    return render(request, 'draftapp/createteacher.html', {'form': form})


@login_required
def views(request):
    all_students = Student.objects.all()
    template = loader.get_template('draftapp/views.html')
    context = {
        'all_students': all_students,
    }
    return HttpResponse(template.render(context, request))


@login_required
def details(request, Student_ID):
    student = Student.objects.get(id=Student_ID)
    template = loader.get_template('draftapp/details.html')
    context = {
        'student': student
    }
    return HttpResponse(template.render(context,request))


@login_required
def viewt(request):
    all_teachers = Teacher.objects.all()
    template = loader.get_template('draftapp/viewt.html')
    context = {
        'all_teachers': all_teachers,
    }
    return HttpResponse(template.render(context,request))


@login_required
def detailt(request, Teacher_ID):
    teacher = Teacher.objects.get(id=Teacher_ID)
    template = loader.get_template('draftapp/detailt.html')
    context = {
        'teacher': teacher
    }
    return HttpResponse(template.render(context,request))


@login_required
def editt(request, IDofteacher):
    if request.method == 'POST':  # post or get, s7ab men html w zetta bel database, get ye3ne jib men db w cout

        form = CreateTeacherForm(instance=Teacher.objects.get(id=IDofteacher), data=request.POST)  #
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect("/registration/teacher/{}".format(IDofteacher))
    else:
        form = CreateTeacherForm(instance=Teacher.objects.get(id=IDofteacher))
    return render(request, 'draftapp/editt.html', {'form': form})


@login_required
def edits(request, IDofstudent):
    if request.method == 'POST':

        form = CreateStudentForm(instance=Student.objects.get(id=IDofstudent), data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

    else:
        form = CreateStudentForm(instance=Student.objects.get(id=IDofstudent))
    return render(request, 'draftapp/edits.html', {'form': form})


@login_required
def deleteds(request, studentdelete):
    Student.objects.get(id=studentdelete).delete()
    return HttpResponseRedirect("/registration/views")


@login_required
def deletedt(request, teacherdelete):
    Teacher.objects.get(id=teacherdelete).delete()
    return HttpResponseRedirect("/registration/viewt")








