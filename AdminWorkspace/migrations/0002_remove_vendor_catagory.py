# Generated by Django 2.1.2 on 2019-06-18 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminWorkspace', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='catagory',
        ),
    ]
