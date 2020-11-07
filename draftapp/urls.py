from django.conf.urls import url
from django.urls import path
from .views import adds
from .views import addt
from .views import reghome
from .views import views, viewt
from .views import detailt, details, editt, edits, deleteds, deletedt


urlpatterns = [
    path('', reghome, name='reghome'),
    path('adds', adds, name='adds'),
    path('addt', addt, name='addt'),
    path('views', views, name='views'),
    path('viewt', viewt, name='viewt'),
    url(r'^student/(?P<Student_ID>[0-9]+)/$', details, name='details'),
    url(r'^teacher/(?P<Teacher_ID>[0-9]+)/$', detailt, name='detailt'),
    url(r'^teacher/edit/(?P<IDofteacher>[0-9]+)/$', editt, name='editt'),
    url(r'^student/edit/(?P<IDofstudent>[0-9]+)$', edits, name='edits'),
    url(r'^deleteds/(?P<studentdelete>[0-9]+)$', deleteds, name='deleteds'),
    url(r'^deletedt/(?P<teacherdelete>[0-9]+)$', deletedt, name='deletedt'),
    # url(r'^editg/(?P<IDofstudent>[0-9]+)$', editg, name='editg'),
]
