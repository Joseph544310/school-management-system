from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='grading-home'),
    url(r'^addg/(?P<student_id>[0-9]+)$', addg, name='addg'),
    url(r'^student/(?P<student_id>[0-9]+)$', student_grade, name='student_grade'),
    url(r'^grades/(?P<grade_number>[0-9]+)/$', grade, name='grade'),
]
