# Generated by Django 4.1.5 on 2023-05-10 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("research", "0004_alter_papers_paper"),
    ]

    operations = [
        migrations.AddField(
            model_name="research",
            name="link",
            field=models.URLField(blank=True),
        ),
    ]