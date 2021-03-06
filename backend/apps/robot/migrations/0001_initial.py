# Generated by Django 2.2.4 on 2021-04-28 22:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('strategy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('use_socket', models.BooleanField(default=False)),
                ('cryptopair', models.CharField(default='BTC-USD', max_length=256)),
                ('exchange', models.CharField(default='Bittrex', max_length=256)),
                ('strategy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='strategy.Strategy')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
