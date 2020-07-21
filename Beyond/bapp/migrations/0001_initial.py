# Generated by Django 3.0.7 on 2020-07-20 14:01

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
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('comname', models.CharField(max_length=200)),
            ],
        ),
    ]