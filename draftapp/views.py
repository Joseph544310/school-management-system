from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import CreateStudentForm
from .forms import CreateTeacherForm
# from .forms import CreateGradeForm
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
            formdata = form.cleaned_data
            First_Name= formdata['First_Name']
            Last_Name = formdata['Last_Name']
            # Student_ID = formdata['Student_ID']
            Sex = formdata['Sex']
            Grade = formdata['Grade']
            Nationality= formdata['Nationality']
            Born_in= formdata['Born_in']
            Father= formdata['Father']
            Mother= formdata['Mother']
            City= formdata['City']
            Address= formdata['Address']
            Building= formdata['Building']
            Floor= formdata['Floor']
            Fixed= formdata['Fixed']
            Mobile= formdata['Mobile']
            Medical_state= formdata['Medical_state']
            Student_Bloodtype= formdata['Student_Bloodtype']
            Guardian = formdata['Guardian']
            Guardian_Phone = formdata['Guardian_Phone']
            Guardian_Level_of_Education= formdata['Guardian_Level_of_Education']
            Guardian_City= formdata['Guardian_City']
            Guardian_Address= formdata['Guardian_Address']
            Guardian_Building= formdata['Guardian_Building']
            Student.objects.create(First_Name=First_Name, Last_Name=Last_Name, Sex=Sex, Grade=Grade, Nationality=Nationality, Born_in=Born_in, Father=Father, Mother=Mother, City=City, Address=Address, Building=Building, Floor=Floor, Fixed=Fixed, Mobile=Mobile, Medical_state=Medical_state, Student_Bloodtype=Student_Bloodtype, Guardian=Guardian, Guardian_Phone=Guardian_Phone, Guardian_Level_of_Education=Guardian_Level_of_Education, Guardian_City=Guardian_City, Guardian_Address=Guardian_Address, Guardian_Building=Guardian_Building)
            return HttpResponseRedirect('/registration/views')
    else:
        form = CreateStudentForm()
    return render(request, 'draftapp/createstudent.html', {'form': form})


@login_required
def addt(request):
    if request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            First_Name= formdata['First_Name']
            Last_Name = formdata['Last_Name']
            # Teacher_ID= formdata['Teacher_ID']
            Subject= formdata['Subject']
            Sex= formdata['Sex']
            Nationality= formdata['Nationality']
            Born_in= formdata['Born_in']
            City= formdata['City']
            Address= formdata['Address']
            Building= formdata['Building']
            Floor=formdata['Floor']
            Fixed=formdata['Fixed']
            Mobile=formdata['Mobile']
            Bloodtype=formdata['Bloodtype']
            Teacher.objects.create(First_Name=First_Name, Last_Name=Last_Name, Subject=Subject, Sex=Sex, Nationality=Nationality, Born_in=Born_in, City=City, Address=Address, Building=Building, Floor=Floor, Fixed=Fixed, Mobile=Mobile, Bloodtype=Bloodtype)    #3am ya3mel fat7a isma book bel db
            return HttpResponseRedirect('/registration/viewt')
    else:
        form = CreateTeacherForm()
    return render(request, 'draftapp/createteacher.html', {'form': form})


@login_required
def views(request):
    all_students= Student.objects.all()
    template= loader.get_template('draftapp/views.html')
    context= {
        'all_students': all_students,
    }
    return HttpResponse(template.render(context,request))


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

        form = CreateTeacherForm(request.POST)  #
        if form.is_valid():
            formdata = form.cleaned_data  # erase whatever there was there
            First_Name = formdata['First_Name']  # osas l fat7a l badna nefta7a
            Last_Name = formdata['Last_Name']  ##same same
            # Teacher_ID = formdata['Teacher_ID']
            Subject = formdata['Subject']
            Sex = formdata['Sex']
            Nationality = formdata['Nationality']
            Born_in = formdata['Born_in']
            City = formdata['City']
            Address = formdata['Address']
            Building = formdata['Building']
            Floor = formdata['Floor']
            Fixed = formdata['Fixed']
            Mobile = formdata['Mobile']
            Bloodtype = formdata['Bloodtype']
            teacher = Teacher.objects.get(id=IDofteacher)
            teacher.First_Name=First_Name
            teacher.Last_Name=Last_Name
            # teacher.Teacher_ID=Teacher_ID
            teacher.Subject=Subject
            teacher.Sex=Sex
            teacher.Nationality=Nationality
            teacher.Born_in=Born_in
            teacher.City=City
            teacher.Address=Address
            teacher.Building=Building
            teacher.Floor=Floor
            teacher.Fixed=Fixed
            teacher.Mobile=Mobile
            teacher.Bloodtype=Bloodtype
            Teacher.objects.get(id=IDofteacher).delete()
            teacher.save()

            return HttpResponseRedirect("/registration/teacher/{}".format(IDofteacher))
    else:
        form = CreateTeacherForm()
        form.initialize(IDofteacher)
    return render(request, 'draftapp/editt.html', {'form': form})


@login_required
def edits(request, IDofstudent):
    if request.method == 'POST':

        form = CreateStudentForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            First_Name = formdata['First_Name']
            Last_Name = formdata['Last_Name']
            # Student_ID = formdata['Student_ID']
            Sex = formdata['Sex']
            Grade = formdata['Grade']
            Nationality = formdata['Nationality']
            Born_in = formdata['Born_in']
            Father=formdata['Father']
            Mother=formdata['Mother']
            City = formdata['City']
            Address = formdata['Address']
            Building = formdata['Building']
            Floor = formdata['Floor']
            Fixed = formdata['Fixed']
            Mobile = formdata['Mobile']
            Medical_state=formdata['Medical_state']
            Student_Bloodtype = formdata['Student_Bloodtype']
            Guardian=formdata['Guardian']
            Guardian_Phone=formdata['Guardian_Phone']
            Guardian_Level_of_Education=formdata['Guardian_Level_of_Education']
            Guardian_City = formdata['Guardian_City']
            Guardian_Address = formdata['Guardian_Address']
            Guardian_Building = formdata['Guardian_Building']

            student = Student.objects.get(id=IDofstudent)
            try:
                student.First_Name=First_Name
                student.Last_Name=Last_Name
                # student.Student_ID=Student_ID
                student.Sex=Sex
                student.Grade=Grade
                student.Nationality=Nationality
                student.Born_in=Born_in
                student.Father=Father
                student.Mother=Mother
                student.City=City
                student.Address=Address
                student.Building=Building
                student.Floor=Floor
                student.Fixed=Fixed
                student.Mobile=Mobile
                student.Medical_state=Medical_state
                student.Student_Bloodtype=Student_Bloodtype
                student.Guardian=Guardian
                student.Guardian_Phone=Guardian_Phone
                student.Guardian_Level_of_Education=Guardian_Level_of_Education
                student.Guardian_City=Guardian_City
                student.Guardian_Address=Guardian_Address
                student.Guardian_Building=Guardian_Building
                Student.objects.get(id=IDofstudent).delete()
                student.save()

                return HttpResponseRedirect("/registration/student/{}".format(IDofstudent))
            except:
                return render(request, 'draftapp/error.html', {'message': "ID already exists"})
    else:
        form = CreateStudentForm()
        form.initialize(IDofstudent)
    return render(request, 'draftapp/edits.html', {'form': form})


@login_required
def deleteds(request, studentdelete):
    Student.objects.get(id=studentdelete).delete()
    return HttpResponseRedirect("/registration/views")


@login_required
def deletedt(request, teacherdelete):
    Teacher.objects.get(id=teacherdelete).delete()
    return HttpResponseRedirect("/registration/viewt")








