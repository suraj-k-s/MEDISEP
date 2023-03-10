# Generated by Django 4.1.2 on 2022-10-31 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employee', '0001_initial'),
        ('Admin', '0001_initial'),
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('date', models.DateField(auto_now=True)),
                ('Member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.mem_registration')),
                ('consultancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.consultancy_registration')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor_registration')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.hos_registration')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(null=True)),
                ('date', models.DateField(auto_now=True)),
                ('reply', models.TextField(null=True)),
                ('c_status', models.IntegerField(default=0)),
                ('Member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.mem_registration')),
                ('complainttype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.cmptype')),
                ('consultancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.consultancy_registration')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.hos_registration')),
            ],
        ),
    ]
