# Generated by Django 3.1.7 on 2021-04-07 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_library'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
