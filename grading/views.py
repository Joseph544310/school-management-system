from django.shortcuts import render
from .forms import CreateGradeForm
from .models import Grade
from draftapp.models import Student
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'grading/home.html')


@login_required
def addg(request, student_id):
    if request.method == "POST":
        form = CreateGradeForm(data=request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            Semester = formdata['Semester']
            Math_Grade = formdata['Math_Grade']
            Physics_Grade = formdata['Physics_Grade']
            Chemistry_Grade = formdata['Chemistry_Grade']
            English_Grade = formdata['English_Grade']
            Arabic_Grade = formdata['Arabic_Grade']
            History_Grade = formdata['History_Grade']
            Geography_Grade = formdata['Geography_Grade']
            Tarbiya_Grade = formdata['Tarbiya_Grade']
            Average = (Math_Grade + Physics_Grade + Chemistry_Grade + English_Grade + Arabic_Grade + History_Grade + Geography_Grade + Tarbiya_Grade) / 8
            try:
                student = Student.objects.get(id=student_id)
            except Student.DoesNotExist:
                return render(request, 'grading/notfound.html', {'message': "ID not found"})
            try:
                grade = Grade.objects.get(Student=student, Semester=Semester)
                grade.delete()
                Grade.objects.create(Student=student, Semester=Semester, Math_Grade=Math_Grade, Physics_Grade=Physics_Grade, Chemistry_Grade=Chemistry_Grade, English_Grade=English_Grade, Arabic_Grade=Arabic_Grade, History_Grade=History_Grade, Geography_Grade=Geography_Grade, Tarbiya_Grade=Tarbiya_Grade, Average=Average)
            except Grade.DoesNotExist:
                Grade.objects.create(Student=student, Semester=Semester, Math_Grade=Math_Grade, Physics_Grade=Physics_Grade, Chemistry_Grade=Chemistry_Grade, English_Grade=English_Grade, Arabic_Grade=Arabic_Grade, History_Grade=History_Grade, Geography_Grade=Geography_Grade, Tarbiya_Grade=Tarbiya_Grade, Average=Average)

        return student_grade(request, student_id)
    else:
        form = CreateGradeForm()
    return render(request, 'grading/addg.html', {'form': form})


def grade(request, grade_number):
    all_students = Student.objects.filter(Grade=grade_number)
    context = {
        'all_students': all_students,
        'grade_number': grade_number
    }
    return render(request, 'grading/grade.html', context)


def student_grade(request, student_id):
    student = Student.objects.get(id=student_id)
    try:
        semester_1_grades = Grade.objects.get(Student=student, Semester=1)
    except Grade.DoesNotExist:
        semester_1_grades = False
    try:
        semester_2_grades = Grade.objects.get(Student=student, Semester=2)
    except Grade.DoesNotExist:
        semester_2_grades = False
    try:
        semester_3_grades = Grade.objects.get(Student=student, Semester=3)
    except Grade.DoesNotExist:
        semester_3_grades = False

    context = {
        'student': student,
        'semester_1_grades': semester_1_grades,
        'semester_2_grades': semester_2_grades,
        'semester_3_grades': semester_3_grades
    }
    return render(request, 'grading/studentgrade.html', context)








