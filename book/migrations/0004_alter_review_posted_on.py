# Generated by Django 5.0 on 2024-02-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0003_alter_review_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="posted_on",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
