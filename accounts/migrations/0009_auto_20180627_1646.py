# Generated by Django 2.0.6 on 2018-06-27 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_userprofile_skills'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='owner',
            new_name='user',
        ),
    ]
