# Generated by Django 2.2.5 on 2019-09-12 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ubicaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('cultivo', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
    ]