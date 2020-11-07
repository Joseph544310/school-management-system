from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='financial-home'),
    path('unpaid/', views.unpaid, name='financial-unpaid'),
    path('addpayment/', views.add_payment, name='financial-addpayment'),
    path('checkbalance/', views.check_balance, name='financial-checkbalance'),
    path('addrecord/', views.add_record, name='financial-addrecord'),
    path('deleterecord/', views.delete_record, name='financial-deleterecord'),
    url(r'^checkbalance/(?P<Student_ID>[0-9]+)/$', views.detail_balance, name='details'),
]
