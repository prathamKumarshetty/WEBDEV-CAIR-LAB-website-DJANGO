from django.shortcuts import render, HttpResponse, redirect
from django.db import models  # Add this import
from home.models import Contact, Faculty, RU, Publications  # Ensure Publications is imported
from datetime import datetime
from django.contrib import messages
from math import ceil
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PublicationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PublicationForm, StudentForm, REUForm
from .models import Activity
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm

def view_page(request):
    return render(request, 'base1.html')

def log_activity(user, activity_type, description):
    Activity.objects.create(user=user, activity_type=activity_type, description=description)


def FacultyRegister(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account till it is approved
            user.save()
            messages.success(request, 'Registration successful. Please wait for approval.')
            return redirect('FacultyLogin')
    else:
        form = UserCreationForm()
    return render(request, 'FacultyRegister.html', {'form': form})

@login_required
def approve_users(request):
    if request.user.is_staff:
        pending_users = User.objects.filter(is_active=False)
        if request.method == 'POST':
            user_id = request.POST.get('user_id')
            user = User.objects.get(pk=user_id)
            user.is_active = True
            user.save()
            messages.success(request, f'User {user.username} has been approved.')
            return redirect('approve_users')
        return render(request, 'approve_users.html', {'pending_users': pending_users})
    else:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('home')


def FacultyLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('faculty_home')
            else:
                messages.error(request, 'Account not activated. Please wait for approval.')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'FacultyLogin.html')

@login_required
def faculty_home(request):
    user = request.user
    recent_activities = Activity.objects.filter(user=user).order_by('-timestamp')[:10]
    return render(request, 'faculty_home.html', {
        'user': user,
        'recent_activities': recent_activities
    })


@login_required
def add_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            log_activity(request.user, 'Add Publication', 'Added a new publication.')
            messages.success(request, 'Publication added successfully.')
            return redirect('faculty_home')  # Redirect to faculty home page after submission
    else:
        form = PublicationForm()
    return render(request, 'add_publication.html', {'form': form})

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            log_activity(request.user, 'Add Student', 'Added a new student.')
            messages.success(request, 'Student added successfully.')
            return redirect('faculty_home')  # Redirect to faculty home page after submission
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

@login_required
def add_reu(request):
    if request.method == 'POST':
        form = REUForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            log_activity(request.user, 'Add REU', 'Added a new REU.')
            messages.success(request, 'REU added successfully.')
            return redirect('faculty_home')  # Redirect to faculty home page after submission
    else:
        form = REUForm()
    return render(request, 'add_reu.html', {'form': form})

@login_required
def faculty_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('FacultyLogin')

@login_required
def faculty_logout_admin(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('admin:index')

# Create your views here.
def home(request):
    return render(request, "base1.html")



def analysis(request):
    year = request.GET.get('year')
    if year:
        publications = Publications.objects.filter(year=year)
    else:
        publications = Publications.objects.all()

    quartile_distribution = publications.values('Publication_quartile').annotate(count=models.Count('Publication_quartile'))
    years = Publications.objects.values_list('year', flat=True).distinct()

    # Debugging output
    print("Quartile distribution:", list(quartile_distribution))
    print("Years available:", list(years))

    context = {
        'publications': publications,
        'quartile_distribution': quartile_distribution,
        'years': years,
    }

    return render(request, "analysis.html", context)

def about(request):
    faculty = Faculty.objects.all().order_by('priority')  # Order by priority field
    context = {
        'faculty': faculty,
    }
    return render(request, 'about.html', context)

def AIML(request):
    faculties = Faculty.objects.filter(Faculty_domain='EDGE-AI').order_by('priority')  # Order by priority field
    n = len(faculties)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides + 1), 'faculty': faculties}
    return render(request, "AIML.html", params)

def CLOUD(request):
    faculties = Faculty.objects.filter(Faculty_domain='CLOUD').order_by('priority')  # Order by priority field
    n = len(faculties)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides + 1), 'faculty': faculties}
    return render(request, "CLOUD.html", params)

def HPC(request):
    faculties = Faculty.objects.filter(Faculty_domain='HPC').order_by('priority')  # Order by priority field
    n = len(faculties)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides + 1), 'faculty': faculties}
    return render(request, "HPC.html", params)

def DATASCIENCE(request):
    faculties = Faculty.objects.filter(Faculty_domain='DATA SCIENCE').order_by('priority')  # Order by priority field
    n = len(faculties)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides + 1), 'faculty': faculties}
    return render(request, "DATASCIENCE.html", params)



def OTHER(request):
    return render(request, "OTHER.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        # Check if all required fields are filled
        if name and email and phone and desc:
            # Create and save the Contact object
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            messages.success(request, "Your Message Has Been Sent.")
        else:
            messages.success(request, "Your Message Has not been Sent.")
    
    return render(request, "contact.html")



def research_domains(request):
    faculties = Faculty.objects.all()
    return render(request, 'AIML.html', {'faculties': faculties})

def aiml_view(request):
    faculties = [
        # Replace this with your actual data
        {'name': 'Faculty 1', 'domain': 'AI', 'description': 'Expert in AI', 'link': '#', 'image': {'url': 'url-to-image-1'}},
        {'name': 'Faculty 2', 'domain': 'ML', 'description': 'Expert in ML', 'link': '#', 'image': {'url': 'url-to-image-2'}}
    ]
    return render(request, 'AIML.html', {'faculties': faculties})

def hpc_view(request):
    faculties = [
        # Replace this with your actual data
        {'name': 'Faculty 1', 'domain': 'HPC', 'description': 'Expert in HPC', 'link': '#', 'image': {'url': 'url-to-hpc-image-1'}},
        {'name': 'Faculty 2', 'domain': 'HPC', 'description': 'Expert in HPC', 'link': '#', 'image': {'url': 'url-to-hpc-image-2'}}
    ]
    return render(request, 'HPC.html', {'faculties': faculties})

def cloud_view(request):
    faculties = [
        # Replace this with your actual data
        {'name': 'Faculty 1', 'domain': 'CLOUD', 'description': 'Expert in Cloud Computing', 'link': '#', 'image': {'url': 'url-to-cloud-image-1'}},
        {'name': 'Faculty 2', 'domain': 'CLOUD', 'description': 'Expert in Cloud Computing', 'link': '#', 'image': {'url': 'url-to-cloud-image-2'}}
    ]
    return render(request, 'CLOUD.html', {'faculties': faculties})

def data_science_view(request):
    faculties = [
        # Replace this with your actual data
        {'name': 'Faculty 1', 'domain': 'DATASCIENCE', 'description': 'Expert in Data Science', 'link': '#', 'image': {'url': 'url-to-datascience-image-1'}},
        {'name': 'Faculty 2', 'domain': 'DATASCIENCE', 'description': 'Expert in Data Science', 'link': '#', 'image': {'url': 'url-to-datascience-image-2'}}
    ]
    return render(request, 'DATASCIENCE.html', {'faculties': faculties})




def MINIOR(request):
    return render(request, "MINIOR.html")

def PUBLICATIONS(request):
    year = request.GET.get('year')
    if year:
        publications = Publications.objects.filter(year=year)
    else:
        publications = Publications.objects.all()

    quartile_distribution = publications.values('Publication_quartile').annotate(count=models.Count('Publication_quartile'))

    context = {
        'publications': publications,
        'quartile_distribution': quartile_distribution,
        'years': Publications.objects.values_list('year', flat=True).distinct()
    }
    return render(request, "PUBLICATIONS.html", context)

def MINI(request):
    return render(request, "MINI.html")

def COURSE_PROJECT(request):
    return render(request, "COURSE_PROJECT.html")

def FACULTY(request):
    return render(request, "FACULTY.html")

def REU(request):
    query = request.GET.get('query')
    year = request.GET.get('year')

    results = RU.objects.all()
    
    if query:
        results = results.filter(

            models.Q(year__icontains=query) |
            models.Q(REU_topic__icontains=query) |
            models.Q(name_of_the_student__icontains=query) |
            models.Q(guide_name__icontains=query) |
            models.Q(co_guide_name__icontains=query) |
            models.Q(SRN__icontains=query)
        )
    
    if year:
        results = results.filter(year=year)

    context = {
        'results': results,
        'years': RU.objects.values_list('year', flat=True).distinct()
    }
    return render(request, "REU.html", context)
