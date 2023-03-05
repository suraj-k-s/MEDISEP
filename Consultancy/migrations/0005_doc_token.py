# Generated by Django 4.1.2 on 2022-10-31 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Consultancy', '0004_delete_doc_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc_Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_no', models.CharField(max_length=50)),
                ('Token_Booking_status', models.IntegerField(default=0)),
                ('Dr_availability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Consultancy.dr_availability')),
            ],
        ),
    ]