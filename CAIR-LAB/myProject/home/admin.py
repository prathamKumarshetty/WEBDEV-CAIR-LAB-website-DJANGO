from django.contrib import admin
from .models import Contact, Faculty, Student, Publications, RU

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('Faculty_name', 'Faculty_domain')
    search_fields = ('Faculty_name', 'Faculty_domain')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('Student_name', 'Student_roll_no', 'Student_phone_no', 'Rid')
    search_fields = ('Student_name', 'Student_roll_no')
    list_filter = ('Rid',)

class PublicationsAdmin(admin.ModelAdmin):
    list_display = ('Publication_name', 'year')
    search_fields = ('Publication_name', 'year', 'faculty_authors__Faculty_name', 'student_authors__Student_name')
    filter_horizontal = ('faculty_authors', 'student_authors')  # Add this to enable a widget for many-to-many fields

class RUAdmin(admin.ModelAdmin):
    list_display = ('RU_id', 'guide_name', 'co_guide_name', 'name_of_the_student', 'SRN', 'REU_topic', 'year', 'RU_domain')
    search_fields = ('RU_domain', 'name_of_the_student', 'guide_name', 'co_guide_name', 'SRN', 'REU_topic', 'year')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Publications, PublicationsAdmin)
admin.site.register(RU, RUAdmin)
