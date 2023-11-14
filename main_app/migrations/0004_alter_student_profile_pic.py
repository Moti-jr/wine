# Generated by Django 4.2.7 on 2023-11-13 12:17

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_student_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=main_app.models.generate_unique_name),
        ),
    ]