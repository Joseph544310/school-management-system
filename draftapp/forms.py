from django import forms
from .models import Student
from .models import Teacher


class CreateStudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['First_Name', 'Last_Name', 'Sex', 'Grade', 'Nationality', 'Born_in', 'Father', 'Mother', 'City',
                  'Address', 'Building', 'Floor', 'Fixed', 'Mobile', 'Medical_state', 'Student_Bloodtype',
                  'Guardian', 'Guardian_Phone', 'Guardian_Level_of_Education', 'Guardian_City', 'Guardian_Address',
                  'Guardian_Building', 'Guardian_Bloodtype']


class CreateTeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ['First_Name', 'Last_Name', 'Subject', 'Sex', 'Nationality', 'Born_in', 'City',
                  'Address', 'Building', 'Floor', 'Fixed', 'Mobile', 'Bloodtype']
