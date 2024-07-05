from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"


class Contact(models.Model):
    name = models.CharField(max_length=122, default='nan')
    email = models.CharField(max_length=122, default='nan')
    phone = models.CharField(max_length=12, default='nan')
    desc = models.TextField(default='nan')

    def __str__(self):
        return self.name


class Faculty(models.Model):
    FACULTY_DOMAIN_CHOICES = [
        ('EDGE-AI', 'EDGE-AI'),
        ('HPC', 'HPC'),
        ('CLOUD', 'CLOUD'),
        ('DATA SCIENCE', 'DATA SCIENCE'),
    ]

    Faculty_id = models.AutoField(primary_key=True)
    Faculty_name = models.CharField(max_length=100, default='nan')
    Faculty_domain = models.CharField(max_length=50, choices=FACULTY_DOMAIN_CHOICES, default='EDGE-AI')
    Faculty_image = models.ImageField(upload_to="faculty/images", default="images/default_image.png")
    Faculty_description = models.TextField(default='nan')
    Faculty_pass = models.CharField(max_length=100, default='nan')
    priority = models.IntegerField(default=0)  # Add this line to include priority field

    def __str__(self):
        return self.Faculty_name


class Student(models.Model):
    Student_id = models.AutoField(primary_key=True)
    Student_name = models.CharField(max_length=100, default='nan')
    Student_roll_no = models.CharField(max_length=20, default='nan')
    Student_image = models.ImageField(upload_to="students/images", default="images/default_image.png")
    Student_phone_no = models.CharField(max_length=15, default='nan')
    Rid = models.BooleanField(default=False)

    def __str__(self):
        return self.Student_name


class RU(models.Model):
    RU_id = models.AutoField(primary_key=True)
    guide_name = models.CharField(max_length=100, default='nan')  # Default value added
    co_guide_name = models.CharField(max_length=100, blank=True, null=True, default='nan')  # Default value added
    name_of_the_student = models.CharField(max_length=100, default='nan')  # Default value added
    SRN = models.CharField(max_length=20, default='nan')  # Default value added
    REU_topic = models.TextField(default='nan')  # Default value added
    year = models.IntegerField(default=2023)  # New field added
    Student_id = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    Faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank=True, null=True)
    RU_domain = models.CharField(max_length=255, default='nan')
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Add this line to include phone number field

    def __str__(self):
        return f"RU {self.RU_id} - {self.RU_domain} (Student: {self.name_of_the_student})"


class Publications(models.Model):
    PUBLICATION_QUARTILE_CHOICES = [
        ('Q1', 'Q1'),
        ('Q2', 'Q2'),
        ('Q3', 'Q3'),
        ('Q4', 'Q4'),
    ]
    
    PUBLICATION_SCOPUS_CHOICES = [
        (True, 'Yes'),
        (False, 'No'),
    ]

    PUBLICATION_TYPE_CHOICES = [
        ('journal', 'Journal'),
        ('conference', 'Conference'),
        ('book_series', 'Book Series'),
        ('transaction', 'Transaction'),
        ('others', 'Others'),
    ]

    PUBLICATION_FIELD_CHOICES = [
        ('faculty', 'Faculty'),
        ('REU', 'REU'),
        ('minor', 'Minor'),
        ('mini', 'Mini'),
        ('course_project', 'Course Project'),
        ('others', 'Others'),
    ]

    PUBLICATION_DOMAIN_CHOICES = [
        ('EDGE-AI', 'EDGE-AI'),
        ('DATA SCIENCE', 'DATA SCIENCE'),
        ('CLOUD', 'CLOUD'),
        ('HPC', 'HPC'),
    ]

    AUTHOR_TYPE_CHOICES = [
        ('faculty', 'Faculty'),
        ('student', 'Student'),
    ]

    Publication_id = models.AutoField(primary_key=True)
    Publication_name = models.CharField(max_length=255, default='nan')
    Publication_scopus = models.BooleanField(choices=PUBLICATION_SCOPUS_CHOICES, default=False)
    Publication_quartile = models.CharField(max_length=2, choices=PUBLICATION_QUARTILE_CHOICES, default='Q1')
    Publication_pdf = models.FileField(upload_to="publications/pdfs", default="publications/pdfs/default_pdf.pdf")
    Publication_type = models.CharField(max_length=20, choices=PUBLICATION_TYPE_CHOICES, default='journal')
    Publication_field = models.CharField(max_length=20, choices=PUBLICATION_FIELD_CHOICES, default='REU')
    Publication_domain = models.CharField(max_length=50, choices=PUBLICATION_DOMAIN_CHOICES, default='EDGE-AI')
    paper_link = models.URLField(max_length=200, default="https://default-link.com")
    year = models.IntegerField(default=2023)
    faculty_authors = models.ManyToManyField(Faculty, related_name='publications_faculty')
    student_authors = models.ManyToManyField(Student, related_name='publications_student')

    def __str__(self):
        return self.Publication_name
