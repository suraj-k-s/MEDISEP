# Generated by Django 4.1.3 on 2022-11-05 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VIEW_MEMBERDETAILS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mem_relation', models.CharField(max_length=50)),
                ('Mem_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Employee.mem_registration')),
            ],
        ),
    ]
