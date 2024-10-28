# Generated by Django 4.2.16 on 2024-09-23 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=200)),
                ('cus_email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('cus_age', models.IntegerField()),
                ('cus_address', models.TextField()),
            ],
        ),
    ]
