# Generated by Django 4.0.5 on 2022-07-10 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Homeapp', '0011_alter_borrowedbooks_bks_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedbooks',
            name='bks_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='bookid', serialize=False, to='Homeapp.books'),
        ),
    ]