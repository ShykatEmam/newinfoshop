# Generated by Django 4.0.1 on 2022-01-26 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0011_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingmalls',
            old_name='title',
            new_name='title_new',
        ),
    ]
