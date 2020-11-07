from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import log_in, log_out

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('', log_in, name='login'),
    path('home/', include('home.urls')),
    # path('logout/', auth_views.LogoutView.as_view(template_name='authentication/logout.html'), name='logout'),
    path('logout/', log_out, name='logout'),
    path('registration/', include('draftapp.urls')),
    path('financial/', include('financial.urls')),
    path('grading/', include('grading.urls')),
    path('home/', include('home.urls')),

]
