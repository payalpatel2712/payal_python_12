# Generated by Django 4.0.5 on 2022-07-21 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_patient_name_appointment_patient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='precription',
        ),
    ]