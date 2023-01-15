# Generated by Django 4.0.4 on 2022-06-01 19:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('berrylush_app', '0002_rename_reviews_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('bio', models.TextField(blank=True, max_length=256, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]