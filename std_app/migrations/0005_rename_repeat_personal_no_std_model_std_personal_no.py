# Generated by Django 4.0.5 on 2022-07-09 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('std_app', '0004_std_model_repeat_personal_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='std_model',
            old_name='repeat_personal_No',
            new_name='std_personal_No',
        ),
    ]
