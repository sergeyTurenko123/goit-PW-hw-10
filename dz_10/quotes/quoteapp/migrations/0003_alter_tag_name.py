# Generated by Django 5.0.6 on 2024-06-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quoteapp", "0002_rename_autor_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]