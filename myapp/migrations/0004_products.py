# Generated by Django 4.2.14 on 2024-10-17 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=200)),
                ('p_desc', models.TextField()),
                ('p_rate', models.IntegerField()),
                ('p_image', models.ImageField(upload_to='static/products/')),
            ],
        ),
    ]
