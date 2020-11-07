from django import forms


class StudentIdForm(forms.Form):
    student_ID = forms.IntegerField()


class AddPaymentForm(forms.Form):
    student_ID = forms.IntegerField()
    amount_Paid = forms.IntegerField()


class AddRecordForm(forms.Form):
    student_ID = forms.IntegerField()
    total_Tuition = forms.IntegerField()
    paid_Amount = forms.IntegerField()


class DeleteRecordForm(forms.Form):
    student_ID = forms.IntegerField()
