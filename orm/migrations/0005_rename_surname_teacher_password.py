# Generated by Django 4.2.3 on 2023-09-20 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0004_remove_student_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='surname',
            new_name='password',
        ),
    ]
