# Generated by Django 4.0.1 on 2022-01-26 08:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0005_shoppingmalls_delete_malls_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('demo_link', models.CharField(max_length=1000)),
                ('source_link', models.CharField(max_length=1000)),
                ('vote_total', models.IntegerField(default=0)),
                ('vote_ratio', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
