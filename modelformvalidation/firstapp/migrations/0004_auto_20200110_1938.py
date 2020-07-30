# Generated by Django 2.2.7 on 2020-01-10 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20200110_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=36)),
                ('user_username', models.CharField(max_length=36)),
                ('user_password', models.CharField(max_length=36)),
                ('user_confirm_password', models.CharField(max_length=36)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_contact', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('idproof_images', models.ImageField(upload_to='idproof/')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
