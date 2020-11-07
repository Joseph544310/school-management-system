from django import forms
from .models import Grade
from draftapp.models import Student


class CreateGradeForm(forms.Form):

    SEMESTER = [
        (1, 1),
        (2, 2),
        (3, 3),
    ]
    Semester = forms.IntegerField(label="Semester", widget=forms.Select(choices=SEMESTER))
    Math_Grade = forms.FloatField(label="Math")
    Physics_Grade = forms.FloatField(label="Physics")
    Chemistry_Grade = forms.FloatField(label="Chemistry")
    English_Grade = forms.FloatField(label="English")
    Arabic_Grade = forms.FloatField(label="Arabic")
    History_Grade = forms.FloatField(label="History")
    Geography_Grade = forms.FloatField(label="Geography")
    Tarbiya_Grade = forms.FloatField(label="Tarbiya")

    def initialize(self, ID):

        data = Grade.objects.get(id=ID)
        # self.fields['Student_ID'].initial = data.Student_ID
        self.fields['Semester'].initial = data.Semester
        self.fields['Math_Grade'].initial = data.Math_Grade
        self.fields['Physics_Grade'].initial = data.Physics_Grade
        self.fields['Chemistry_Grade'].initial = data.Chemistry_Grade
        self.fields['English_Grade'].initial = data.English_Grade
        self.fields['Arabic_Grade'].initial = data.Arabic_Grade
        self.fields['History_Grade'].initial = data.History_Grade
        self.fields['Geography_Grade'].initial = data.Geography_Grade
        self.fields['Tarbiya_Grade'].initial = data.Tarbiya_Grade
