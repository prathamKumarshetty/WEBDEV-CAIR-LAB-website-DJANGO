from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Publications, Faculty, Student, RU

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PublicationForm(forms.ModelForm):
    faculty_authors = forms.ModelMultipleChoiceField(
        queryset=Faculty.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    student_authors = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Publications
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class REUForm(forms.ModelForm):
    class Meta:
        model = RU
        fields = '__all__'
