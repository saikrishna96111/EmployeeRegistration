# Generated by Django 3.2.7 on 2021-11-22 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeHome', '0006_alter_employee_ssn'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Employees',
        ),
    ]