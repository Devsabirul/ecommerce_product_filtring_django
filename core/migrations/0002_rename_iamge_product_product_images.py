# Generated by Django 4.2.1 on 2023-05-27 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="iamge",
            new_name="product_images",
        ),
    ]