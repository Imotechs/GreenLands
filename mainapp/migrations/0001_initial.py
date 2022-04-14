# Generated by Django 4.0.1 on 2022-04-14 12:15

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
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('photo', models.ImageField(default='media/Adverts/default.jpg', upload_to='media/Adverts')),
                ('descriptions', models.TextField()),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AvailableJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('local_govt', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('number_of_workers', models.IntegerField()),
                ('description', models.TextField(default='I have a Job')),
                ('cost', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('photo', models.ImageField(default='media/crops/default.jpg', upload_to='media/crops')),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Farm_Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('photo', models.ImageField(default='media/Farm_tool/default.jpg', upload_to='media/Farm_tool')),
                ('local_govt', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('customer_phone', models.CharField(max_length=15)),
                ('customer_name', models.CharField(max_length=30)),
                ('customer_address', models.CharField(max_length=30)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(default='media/Land/default.jpg', upload_to='media/Land')),
                ('local_govt', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('customer_phone', models.CharField(max_length=15)),
                ('available', models.BooleanField(default=True)),
                ('cost', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_quarter', models.BooleanField(default=True)),
                ('second_quarter', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Trending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('photo', models.ImageField(default='media/Trending/default.jpg', upload_to='media/Trending')),
                ('local_govt', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('offer_season', models.CharField(max_length=20)),
                ('offer_gain', models.CharField(max_length=20)),
                ('offer_duration', models.CharField(max_length=20)),
                ('available', models.BooleanField(default=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('quarter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.quarter')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='media/user_profiles/default.PNG', upload_to='media/user_profiles')),
                ('phone', models.CharField(max_length=15)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AvailableWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('id_card', models.ImageField(default='media/Identities/default.jpg', upload_to='media/Identities')),
                ('id_number', models.CharField(max_length=30)),
                ('description', models.TextField(default='I want to be a worker')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
