# Generated by Django 2.2.16 on 2021-02-05 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("candidates", "0064_loggedaction_approved")]

    operations = [
        migrations.AddField(
            model_name="ballot",
            name="replaces",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="replaced_by",
                to="candidates.Ballot",
            ),
        )
    ]
