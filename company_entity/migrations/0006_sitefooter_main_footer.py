# Generated by Django 5.0.4 on 2024-05-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_entity', '0005_alter_company_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitefooter',
            name='main_footer',
            field=models.BooleanField(default=True, verbose_name='Rodapé Principal'),
        ),
    ]