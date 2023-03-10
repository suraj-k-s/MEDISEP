# Generated by Django 4.1.2 on 2022-10-31 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact', models.CharField(max_length=50)),
                ('address', models.TextField(null=True)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to='userdocs/')),
                ('password', models.CharField(max_length=50, unique=True)),
                ('doj', models.DateField(auto_now_add=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.place')),
            ],
        ),
    ]
