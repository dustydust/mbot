# Generated by Django 2.2.4 on 2021-04-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategy',
            name='config',
            field=models.TextField(null=True),
        ),
    ]