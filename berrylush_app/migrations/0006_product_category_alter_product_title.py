# Generated by Django 4.0.4 on 2022-06-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berrylush_app', '0005_rename_name_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('jam', 'JAM'), ('berries', 'BERRIES'), ('experiences', 'EXPERIENCES')], max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]