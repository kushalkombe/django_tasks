# Generated by Django 2.2 on 2019-12-04 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=30)),
                ('empid', models.IntegerField()),
                ('empdesg', models.CharField(max_length=50)),
                ('empsal', models.FloatField()),
                ('empaddr', models.TextField()),
            ],
        ),
    ]