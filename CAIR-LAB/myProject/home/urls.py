from django.contrib import admin
from django.urls import path
from home import views
from .views import UserRegistrationForm, approve_users, view_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('FacultyLogin/', views.FacultyLogin, name='FacultyLogin'),
    path('faculty_home/', views.faculty_home, name='faculty_home'),
    path('add_publication/', views.add_publication, name='add_publication'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_reu/', views.add_reu, name='add_reu'),
    path('FACULTY', views.FACULTY, name='FACULTY'),
    path('contact/', views.contact, name='contact'),
    path('faculty_logout/', views.faculty_logout, name='faculty_logout'),
    path('faculty_logout_admin/', views.faculty_logout_admin, name='faculty_logout_admin'),
    path("AIML", views.AIML, name="AIML"),
    path("CLOUD", views.CLOUD, name="CLOUD"),  # Updated URL pattern for CLOUD path
    path("DATASCIENCE", views.DATASCIENCE, name="DATASCIENCE"),
    path("OTHER", views.OTHER, name="OTHER"),
    path("HPC", views.HPC, name="HPC"),
    path("home", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path('research-domains/', views.research_domains, name='research_domains'),
    path('AIML/', views.aiml_view, name='aiml_view'),
    path('HPC/', views.hpc_view, name='hpc_view'),
    path('DATASCIENCE/', views.data_science_view, name='data_science_view'),
    path('CLOUD/', views.cloud_view, name='cloud_view'),
    path("MINIOR", views.MINIOR, name="MINIOR"),
    path("MINI", views.MINI, name="MINI"),
    path("COURSE_PROJECT", views.COURSE_PROJECT, name="COURSE_PROJECT"),
    path("REU", views.REU, name="REU"),
    path("PUBLICATIONS", views.PUBLICATIONS, name="PUBLICATIONS"),
    path("analysis", views.analysis, name="analysis"),
    path('FacultyRegister/', views.FacultyRegister, name='FacultyRegister'),
    path('approve-users/', approve_users, name='approve_users'),
    path('view_page/', view_page, name='view_page'),  # Added view_page URL
]
