# Generated by Django 4.1.2 on 2022-10-31 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Consultancy', '0005_doc_token'),
        ('Doctors', '0002_delete_checkup_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckUp_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_description', models.TextField(null=True)),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc_token', to='Consultancy.doc_token')),
            ],
        ),
    ]