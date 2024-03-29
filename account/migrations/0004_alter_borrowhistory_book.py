# Generated by Django 5.0 on 2024-02-22 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0003_alter_borrowhistory_book"),
        ("book", "0004_alter_review_posted_on"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowhistory",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="book",
                to="book.book",
            ),
        ),
    ]
