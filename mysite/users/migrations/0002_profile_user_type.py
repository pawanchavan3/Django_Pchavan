# Generated by Django 4.2.4 on 2023-10-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(default='users', max_length=200),
        ),
    ]
