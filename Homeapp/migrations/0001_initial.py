# Generated by Django 4.0.5 on 2022-06-29 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=70)),
                ('publication_date', models.DateField()),
                ('subject_area', models.CharField(max_length=70)),
                ('author', models.CharField(max_length=40)),
            ],
        ),
    ]