# Generated by Django 3.1.2 on 2020-10-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neigh', models.CharField(max_length=100)),
                ('str', models.CharField(max_length=100)),
                ('num', models.IntegerField(max_length=3)),
                ('phone', models.IntegerField(max_length=20)),
				#('name', models.CharField(max_length=100)),
            ],
        ),
    ]
