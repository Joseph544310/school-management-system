from django.shortcuts import render
from .models import Tuition
from draftapp.models import Student
from .forms import StudentIdForm, AddPaymentForm, AddRecordForm, DeleteRecordForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse


@login_required
def home(request):
    context = {
        'tuition': Tuition.objects.all()
    }
    return render(request, 'financial/home.html', context)


@login_required
def unpaid(request):
    tuition = []
    for record in Tuition.objects.all():
        if record.paid != record.total:
            tuition.append(record)
    context = {
        'tuition': tuition
    }
    return render(request, 'financial/unpaid.html', context)


@login_required
def check_balance(request):
    all_students = Student.objects.all()
    template = loader.get_template('financial/checkBalance.html')
    context = {
        'all_students': all_students,
    }
    return HttpResponse(template.render(context, request))


@login_required
def detail_balance(request, Student_ID):
    student = Student.objects.get(id=Student_ID)
    try:
        tuition = Tuition.objects.get(student=student)
        paid = tuition.paid
        total = tuition.total
    except Tuition.DoesNotExist:
        total = 0
        paid = 0
    context = {
        'paid': paid,
        'total': total,
        'remaining': total - paid
    }
    return render(request, 'financial/studentbalance.html', context)


@login_required
def add_payment(request):
    if request.method == 'POST':
        form = AddPaymentForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            student_id = formdata['student_ID']
            amount = formdata['amount_Paid']
            try:
                student = Student.objects.get(id=student_id)
            except Student.DoesNotExist:
                return render(request, 'financial/notfound.html', {'message': "ID not found"})
            tuition = Tuition.objects.get(student=student)
            if tuition.paid+amount > tuition.total:
                return render(request, 'financial/notfound.html', {'message': "Payment exceeds remaining fees"})
            elif amount < 0:
                return render(request, 'financial/notfound.html', {'message': "Payment should be positive"})
            tuition.paid = tuition.paid + amount
            tuition.unpaid = tuition.unpaid - amount
            tuition.save()
            total = tuition.total
            paid = tuition.paid
            messages.success(request, 'The payment has been successfully added.')
            unpaidfees = tuition.unpaid
            context = {
                'paid': paid,
                'total': total,
                'unpaid': unpaidfees
            }
        return render(request, 'financial/paymentConfirmation.html')
    else:
        form = AddPaymentForm()
    return render(request, 'financial/addPayment.html', {'form': form})


@login_required
def add_record(request):
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            student_id = formdata['student_ID']
            total = formdata['total_Tuition']
            paid = formdata['paid_Amount']
            if total < 0 or paid < 0:
                return render(request, 'financial/notfound.html', {'message': "Amount should be positive"})
            if paid > total:
                return render(request, 'financial/notfound.html', {'message': "Payment exceeds total fees"})
            try:
                student = Student.objects.get(id=student_id)
            except Student.DoesNotExist:
                return render(request, 'financial/notfound.html', {'message': "ID not found"})
            try:
                tuition = Tuition.objects.get(student=student)
                tuition.delete()
                Tuition.objects.create(student=student, total=total, paid=paid, unpaid=total - paid)
            except Tuition.DoesNotExist:
                Tuition.objects.create(student=student, total=total, paid=paid, unpaid=total - paid)

        return render(request, 'financial/home.html')
    else:
        form = AddRecordForm()
    return render(request, 'financial/addRecord.html', {'form': form})


@login_required
def delete_record(request):
    if request.method == 'POST':
        form = DeleteRecordForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            student_id = formdata['student_ID']
            try:
                student = Student.objects.get(id=student_id)
            except Student.DoesNotExist:
                return render(request, 'financial/notfound.html', {'message': "ID not found"})
            record = Tuition.objects.get(student=student)
            record.delete()
        return render(request, 'financial/home.html')
    else:
        form = DeleteRecordForm()
    return render(request, 'financial/deleteRecord.html', {'form': form})


