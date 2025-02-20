# Generated by Django 2.2.19 on 2021-03-30 07:43

import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("people", "0025_add_name_search_trigger")]

    operations = [
        migrations.CreateModel(
            name="PersonNameSynonym",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "term",
                    django.contrib.postgres.search.SearchQueryField(
                        help_text="The term entered"
                    ),
                ),
                (
                    "synonym",
                    django.contrib.postgres.search.SearchQueryField(
                        help_text="An alternative word for the term"
                    ),
                ),
            ],
            options={"ordering": ("-term",)},
        )
    ]
