# Generated by Django 4.1.6 on 2023-02-08 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_warrior'),
    ]

    operations = [
        migrations.AddField(
            model_name='swordsmith',
            name='warriors',
            field=models.ManyToManyField(to='main_app.warrior'),
        ),
    ]
