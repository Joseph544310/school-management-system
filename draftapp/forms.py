from django import forms
from .models import Student
from .models import Teacher


class CreateStudentForm(forms.Form):

    First_Name = forms.CharField(label='First Name')
    Last_Name = forms.CharField(label='Last Name')
    # Student_ID = forms.IntegerField(label='ID')
    SEX = [
        ("M", "Male"),
        ("F", "Female")
    ]
                                                                         # Sex = forms.CharField(label='Sex', choices=SEX)
    Sex=forms.CharField(label='Sex',widget=forms.Select(choices=SEX))
    GRADE = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12)
    ]
    Grade = forms.IntegerField(label='Grade',widget=forms.Select(choices=GRADE))
    Nationality = forms.CharField(label='Nationality')
    Born_in = forms.IntegerField( label='Born in')                #used to be int
    Father = forms.CharField(label='Father')
    Mother = forms.CharField(label='Mother')
    City = forms.CharField(label='City')
    Address = forms.CharField(label='Address')
    Building = forms.CharField(label='Building')
    Floor = forms.CharField(label='Floor')
    Fixed = forms.IntegerField(label='Fixed')                  #used to be int
    Mobile = forms.IntegerField( label='Mobile')                 #used to be int
    HEALTH = [
        ("H", "Healthy"),
        ("NH", "Sickboi")
    ]
    Medical_state = forms.CharField(max_length=3, label='Medical State', widget=forms.Select(choices=HEALTH))
    Bloodtype = [
        ('A', 'A+'),
        ('A', 'A-'),
        ('B', 'B+'),
        ('B', 'B-'),
        ('AB', 'AB+'),
        ('AB', 'AB-'),
        ('O', 'O+'),
        ('O', 'O-')
    ]
    Student_Bloodtype = forms.CharField(max_length=3, label='Blood Type', widget=forms.Select(choices=Bloodtype))
    MorF = [
        ("M", "Mother"),
        ("F", "Father")
    ]
    Guardian = forms.CharField(label='Guardian', widget=forms.Select(choices=MorF))
    Guardian_Phone = forms.IntegerField( label='Guardian Phone')                    #used to be int
    Guardian_Level_of_Education = forms.CharField(label='Education Level of Guardian')
    Guardian_City = forms.CharField(label='Guardian City')
    Guardian_Address = forms.CharField(label='Guardian Address')
    Guardian_Building = forms.CharField(label='Guardian Building')
    Guardian_Bloodtype = forms.CharField(max_length=3, label='Guardian Bloodtype', widget=forms.Select(choices=Bloodtype))

    def initialize(self, ID):

        data = Student.objects.get(id=ID)
        self.fields['First_Name'].initial = data.First_Name
        self.fields['Last_Name'].initial = data.Last_Name
        # self.fields['Student_ID'].initial = data.Student_ID
        self.fields['Sex'].initial = data.Sex
        self.fields['Grade'].initial = data.Grade
        self.fields['Nationality'].initial = data.Nationality
        self.fields['Born_in'].initial = data.Born_in
        self.fields['Father'].initial = data.Father
        self.fields['Mother'].initial = data.Mother
        self.fields['City'].initial = data.City
        self.fields['Address'].initial = data.Address
        self.fields['Building'].initial = data.Building
        self.fields['Floor'].initial = data.Floor
        self.fields['Fixed'].initial = data.Fixed
        self.fields['Mobile'].initial = data.Mobile
        self.fields['Medical_state'].initial = data.Medical_state
        self.fields['Student_Bloodtype'].initial = data.Student_Bloodtype
        self.fields['Guardian'].initial = data.Guardian
        self.fields['Guardian_Phone'].initial = data.Guardian_Phone
        self.fields['Guardian_Level_of_Education'].initial = data.Guardian_Level_of_Education
        self.fields['Guardian_City'].initial = data.Guardian_City
        self.fields['Guardian_Address'].initial = data.Guardian_Address
        self.fields['Guardian_Building'].initial = data.Guardian_Building
        self.fields['Guardian_Bloodtype'].initial = data.Guardian_Bloodtype


class CreateTeacherForm(forms.Form):
    First_Name = forms.CharField(label='First Name')
    Last_Name = forms.CharField(label='Last Name')
    # Teacher_ID= forms.IntegerField(label='Teacher ID')
    Teaches = [

        ("E", "English"),
        ("E", "Arabic"),
        ("E", "Math"),
        ("E", "Physics"),
        ("E", "Biology"),
        ("E", "Chemistry"),
        ("E", "History"),
        ("E", "Geography"),
        ("E", "Civics"),
        ("E", "Religion"),
        ("E", "PE")
    ]
    Subject = forms.CharField(label='Subject', widget=forms.Select(choices=Teaches))
    SEX = [
        ("M", "Male"),
        ("F", "Female")
    ]
    Sex = forms.CharField(label='Sex', widget=forms.Select(choices=SEX))
    Nationality = forms.CharField(label='Nationality')
    Born_in = forms.IntegerField(label='Born in')                                #used to be int
    City = forms.CharField(label='City')
    Address = forms.CharField(label='Address')
    Building = forms.CharField(label='Building')
    Floor = forms.CharField(label='Floor')
    Fixed = forms.IntegerField(label='Fixed')                                              #used to be int
    Mobile = forms.IntegerField(label='Mobile')                                             #used to be int
    Bloodtype = [
        ('A', 'A+'),
        ('A', 'A-'),
        ('B', 'B+'),
        ('B', 'B-'),
        ('AB', 'AB+'),
        ('AB', 'AB-'),
        ('O', 'O+'),
        ('O', 'O-')
    ]
    Bloodtype = forms.CharField(max_length=3, label='Bloodtype', widget=forms.Select(choices=Bloodtype))

    def initialize(self, ID):

        data = Teacher.objects.get(id=ID)
        self.fields['First_Name'].initial = data.First_Name
        self.fields['Last_Name'].initial = data.Last_Name
        # self.fields['Teacher_ID'].initial = data.Teacher_ID
        self.fields['Subject'].initial = data.Subject
        self.fields['Sex'].initial = data.Sex
        self.fields['Nationality'].initial = data.Nationality
        self.fields['Born_in'].initial = data.Born_in
        self.fields['City'].initial = data.City
        self.fields['Address'].initial = data.Address
        self.fields['Building'].initial = data.Building
        self.fields['Floor'].initial = data.Floor
        self.fields['Fixed'].initial = data.Fixed
        self.fields['Mobile'].initial = data.Mobile
        self.fields['Bloodtype'].initial = data.Bloodtype
