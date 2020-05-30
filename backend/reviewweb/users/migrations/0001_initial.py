# Generated by Django 3.0.3 on 2020-05-27 01:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('D', 'Do not want to select')], default='D', max_length=20)),
                ('dob', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('skintype', models.CharField(choices=[('O', 'Oily'), ('D', 'Dry'), ('C', 'Combinational')], default='C', max_length=20)),
                ('skinshade', models.CharField(choices=[('F', 'Fair'), ('L', 'Light'), ('M', 'Medium'), ('D', 'Dark')], default='F', max_length=20)),
                ('influencer', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=20)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]