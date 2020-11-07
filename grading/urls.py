from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='grading-home'),
    url(r'^addg/(?P<student_id>[0-9]+)$', addg, name='addg'),
    url(r'^student/(?P<student_id>[0-9]+)$', student_grade, name='student_grade'),
    url(r'^grades/(?P<grade_number>[0-9]+)/$', grade, name='grade'),
    # url(r'^teacher/(?P<Teacher_ID>[0-9]+)/$', detailt, name='detailt'),
    # url(r'^teacher/edit/(?P<IDofteacher>[0-9]+)/$', editt, name='editt'),

    # url(r'^deleteds/(?P<studentdelete>[0-9]+)$', deleteds, name='deleteds'),
    # url(r'^deletedt/(?P<teacherdelete>[0-9]+)$', deletedt, name='deletedt'),
    # url(r'^editg/(?P<IDofstudent>[0-9]+)$', editg, name='editg'),
]
