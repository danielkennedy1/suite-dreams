# Generated by Django 4.2 on 2023-04-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="organiser",
            field=models.CharField(default="organiser1", max_length=100),
            preserve_default=False,
        ),
    ]
