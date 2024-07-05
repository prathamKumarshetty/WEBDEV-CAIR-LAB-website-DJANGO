import pandas as pd
from django.core.management.base import BaseCommand
from home.models import Publications

class Command(BaseCommand):
    help = 'Upload publications from an Excel file to the database'

    def handle(self, *args, **kwargs):
        file_path = '/Users/prathamshetty/Desktop/mains/shettys1.0/django1.0/django/myProject/data/cleaned_publication.xlsx'
        df = pd.read_excel(file_path)

        required_columns = [
            'Publication_name', 'Publication_scopus', 'Publication_quartile',
            'Publication_type', 'Publication_field', 'Publication_domain',
            'paper_link', 'year'
        ]

        for column in required_columns:
            if column not in df.columns:
                self.stderr.write(self.style.ERROR(f"Missing required column: {column}"))
                return

        for index, row in df.iterrows():
            publication, created = Publications.objects.update_or_create(
                Publication_name=row['Publication_name'],
                defaults={
                    'Publication_scopus': row['Publication_scopus'],
                    'Publication_quartile': row['Publication_quartile'],
                    'Publication_type': row['Publication_type'],
                    'Publication_field': row['Publication_field'],
                    'Publication_domain': row['Publication_domain'],
                    'paper_link': row['paper_link'],
                    'year': row['year']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully created publication {publication.Publication_name}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Successfully updated publication {publication.Publication_name}"))
