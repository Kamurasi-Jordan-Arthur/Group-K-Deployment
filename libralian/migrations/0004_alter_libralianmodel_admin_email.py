# Generated by Django 4.0.5 on 2022-07-08 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libralian', '0003_libralianmodel_admin_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libralianmodel',
            name='admin_email',
            field=models.EmailField(max_length=254),
        ),
    ]
