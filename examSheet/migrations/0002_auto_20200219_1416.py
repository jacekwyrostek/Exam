# Generated by Django 2.2.6 on 2020-02-19 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examSheet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionsheet',
            old_name='student',
            new_name='owner',
        ),
    ]