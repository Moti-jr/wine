import json
import os.path

from django.core.management import BaseCommand

from database import settings
from main_app.models import Student


class Command(BaseCommand):
    help = 'populate our DB with students data from json file'

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'student.json')
        self.stdout.write(
            self.style.INFO('START INGESTING DATA')
        )
        with open() as file:
            students = json.load(file)
            for s in students:
                Student.objects.create(

                    first_name=s['first_name'],
                    last_name=s['last_name'],
                    email=s['email'],
                    dob=s['dob'],
                    weight=s['weight'],
                    kcpe=s['kcpe_score'],
                    is_spoty=s['is_sporty'],
                    profile_pic=s['student/student.png'],
                )
        self.stdout.write(
            self.style.SUCCESS('COMPLETE INGESTING DATA')
        )