# Generated by Django 2.2 on 2019-05-02 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20190502_2100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='user_id',
            new_name='user',
        ),
    ]
