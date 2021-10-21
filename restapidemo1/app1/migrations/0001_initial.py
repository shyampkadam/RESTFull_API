# Generated by Django 3.2.7 on 2021-10-18 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('email', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=40)),
                ('fullname', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('salary', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]
