# Generated by Django 4.1.2 on 2022-10-31 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Consultancy', '0003_rename_token_doc_token'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doc_Token',
        ),
    ]
