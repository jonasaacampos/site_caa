# Generated by Django 5.0.4 on 2024-05-08 14:13

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_entity', '0009_alter_sitefooter_service_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitefooter',
            name='service_hours',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]
