# Generated by Django 3.2.4 on 2021-10-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("candidates", "0076_ballot_ee_modified")]

    operations = [
        migrations.AddField(
            model_name="loggedaction",
            name="person_pk",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="This is stored to help us identify the related person an action was for after the Person has been deleted",
                null=True,
            ),
        )
    ]
