# Generated by Django 4.1.6 on 2023-04-19 07:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="content",
            field=models.FileField(
                blank=True,
                upload_to="content/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=[
                            ".mp4",
                            ".mov",
                            ".avi",
                            ".wmv",
                            ".mkv",
                            ".flv",
                            ".jpg",
                            ".pdf",
                            ".jpeg",
                            ".png",
                            ".gif",
                            ".bmp",
                            ".svg",
                            ".doc",
                            ".docx",
                            ".txt",
                            ".rtf",
                            ".odt",
                            ".wps",
                            ".ppt",
                            ".pptx",
                            ".odp",
                            ".key",
                            ".cvs",
                            ".txt",
                        ]
                    )
                ],
            ),
        ),
    ]
