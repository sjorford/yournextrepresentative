# Generated by Django 3.2.10 on 2022-02-08 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("official_documents", "0026_remove_null_on_relevant_pages")
    ]

    operations = [
        migrations.AlterField(
            model_name="officialdocument",
            name="source_url",
            field=models.URLField(
                help_text="The URL of this document", max_length=1000
            ),
        )
    ]
