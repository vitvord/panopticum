# Generated by Django 4.2.11 on 2024-04-07 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panopticum', '0012_rename_meta_bad_rating_fields_componentversionmodel_meta_profile_not_signed_requirements_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='componentversionmodel',
            name='meta_mt_rating',
        ),
        migrations.RemoveField(
            model_name='componentversionmodel',
            name='meta_op_rating',
        ),
        migrations.RemoveField(
            model_name='historicalcomponentversionmodel',
            name='meta_mt_rating',
        ),
        migrations.RemoveField(
            model_name='historicalcomponentversionmodel',
            name='meta_op_rating',
        ),
    ]