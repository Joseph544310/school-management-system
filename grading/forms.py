from django import forms


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
