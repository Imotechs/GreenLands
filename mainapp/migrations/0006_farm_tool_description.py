# Generated by Django 4.0.1 on 2022-04-14 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_remove_availablejob_name_availablejob_approved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm_tool',
            name='description',
            field=models.TextField(default='All available Tool at Greenlands'),
        ),
    ]
