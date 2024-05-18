# Generated by Django 5.0.2 on 2024-05-18 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=50)),
                ('pakagetype', models.CharField(max_length=50)),
                ('pakagedetails', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
    ]
