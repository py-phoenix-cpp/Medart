# Generated by Django 4.1.1 on 2022-09-08 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_doctors_detail_doctors_about_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationg_attented',
            name='main_doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.doctors'),
            preserve_default=False,
        ),
    ]
