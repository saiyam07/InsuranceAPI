# Generated by Django 3.1.3 on 2020-11-23 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20201123_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='fuel',
            field=models.CharField(editable=False, max_length=10),
        ),
    ]
