# Generated by Django 3.1.4 on 2021-04-08 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=122)),
                ('lastName', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=6)),
                ('phoneNumber', models.CharField(max_length=13)),
            ],
        ),
    ]
