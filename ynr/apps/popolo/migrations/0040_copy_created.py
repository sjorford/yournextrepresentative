# Generated by Django 2.2.20 on 2021-06-16 15:48

from django.db import migrations

MODELS_TO_UPDATE = ["ContactDetail", "Membership", "Organization", "Post"]


def copy_created_at(apps, schema_editor):
    for ModelClass in MODELS_TO_UPDATE:
        ModelClass = apps.get_model("popolo", ModelClass)
        for obj in ModelClass.objects.iterator():
            obj.created = obj.created_at
            obj.save()


def copy_created(apps, schema_editor):
    for ModelClass in MODELS_TO_UPDATE:
        ModelClass = apps.get_model("popolo", ModelClass)
        for obj in ModelClass.objects.iterator():
            obj.created_at = obj.created
            obj.save()


class Migration(migrations.Migration):

    dependencies = [("popolo", "0039_auto_20210616_1642")]

    operations = [
        migrations.RunPython(code=copy_created_at, reverse_code=copy_created)
    ]
