# Generated by Django 4.2.3 on 2024-08-21 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
