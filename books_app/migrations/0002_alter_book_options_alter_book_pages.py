# Generated by Django 5.1.2 on 2024-10-31 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={"ordering": ["title"]},
        ),
        migrations.AlterField(
            model_name="book",
            name="pages",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
