# Generated by Django 4.1.2 on 2022-10-31 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CMPTYPE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmptype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DISTRICT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DR_DEPARTMENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dr_deptname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EMP_DEPARTMENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_deptname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EMP_GRADEPOST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_gradepost', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EMP_REGISTRATION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_name', models.CharField(max_length=50)),
                ('Emp_address', models.CharField(max_length=50)),
                ('Emp_contact', models.CharField(max_length=50)),
                ('Emp_emailid', models.CharField(max_length=50)),
                ('Emp_gender', models.CharField(max_length=50)),
                ('Emp_age', models.CharField(max_length=50)),
                ('Emp_photo', models.FileField(upload_to='EmployeeDocs/')),
                ('doj', models.DateField(auto_now_add=True)),
                ('PEN_NO', models.CharField(max_length=50)),
                ('Medisep_insurance_id', models.CharField(max_length=50)),
                ('Num_fam_members', models.CharField(max_length=50)),
                ('Emp_password', models.CharField(max_length=50, unique=True)),
                ('Emp_gradepost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.emp_gradepost')),
            ],
        ),
        migrations.CreateModel(
            name='HSPTLTYPE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsptltype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PLACE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.district')),
            ],
        ),
        migrations.CreateModel(
            name='Medisep_Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Insurance_amount', models.CharField(max_length=100)),
                ('Emp_PENo', models.CharField(max_length=50)),
                ('Insurance_PaymentAmount', models.CharField(max_length=100)),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.emp_registration')),
            ],
        ),
        migrations.CreateModel(
            name='HOS_REGISTRATION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hos_name', models.CharField(max_length=50)),
                ('Hos_address', models.TextField(null=True)),
                ('Hos_contact', models.CharField(max_length=50)),
                ('Hos_emailid', models.EmailField(max_length=254, unique=True)),
                ('Hos_logo', models.FileField(upload_to='HospitalDocs/')),
                ('Hos_proof', models.FileField(upload_to='HospitalDocs/')),
                ('Hos_password', models.CharField(max_length=50, unique=True)),
                ('Hos_isactive', models.CharField(max_length=50)),
                ('Hos_establishment', models.DateField()),
                ('Hos_veri_status', models.CharField(max_length=50)),
                ('Hos_Place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.place')),
                ('Hospital_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.hsptltype')),
            ],
        ),
        migrations.CreateModel(
            name='EMP_SUBDEPT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_subdept_name', models.CharField(max_length=50)),
                ('Emp_deptid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.emp_department')),
            ],
        ),
        migrations.AddField(
            model_name='emp_gradepost',
            name='Emp_subdept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.emp_subdept'),
        ),
    ]
