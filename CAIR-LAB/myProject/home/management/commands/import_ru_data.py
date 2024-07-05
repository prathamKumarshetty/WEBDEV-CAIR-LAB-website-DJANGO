import pandas as pd
from django.core.management.base import BaseCommand
from home.models import RU, Student, Faculty

class Command(BaseCommand):
    help = 'Import RU details from an Excel file into the database'

    def add_arguments(self, parser):
        parser.add_argument('/Users/prathamshetty/Desktop/django/myProject/data/REU_excel.xlsx', type=str, help='The path to the Excel file.')

    def handle(self, *args, **kwargs):
        file_path = kwargs['/Users/prathamshetty/Desktop/django/myProject/data/REU_excel.xlsx']
        data = pd.read_excel(file_path)

        for index, row in data.iterrows():
            student, _ = Student.objects.get_or_create(
                Student_name=row['Student Name'], defaults={'Student_roll_no': row['SRN']}
            )
            faculty, _ = Faculty.objects.get_or_create(
                Faculty_name=row['Guide Name']
            )

            co_guide_name = row['Co-Guide Name'] if 'Co-Guide Name' in row and pd.notna(row['Co-Guide Name']) else None

            RU.objects.create(
                guide_name=row['Guide Name'],
                co_guide_name=co_guide_name,
                name_of_the_student=row['Student Name'],
                SRN=row['SRN'],
                REU_topic=row['REU Topic'],
                Student_id=student,
                Faculty_id=faculty,
                RU_domain=row['Domain'],
                year=row['Year']
            )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
