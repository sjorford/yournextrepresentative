# Generated by Django 2.2.18 on 2021-05-13 11:27

from django.db import migrations


def update_versions(versions, current_key, new_key):
    for version in versions:
        for result in version["candidate_results"]:
            try:
                result[new_key] = result.pop(current_key)
            except KeyError:
                continue


def forwards(apps, schema_editor):
    ResultSet = apps.get_model("uk_results", "ResultSet")
    for result in ResultSet.objects.all().iterator():
        update_versions(
            versions=result.versions, current_key="is_winner", new_key="elected"
        )
        result.save()


def backwards(apps, schema_editor):
    ResultSet = apps.get_model("uk_results", "ResultSet")
    for result in ResultSet.objects.iterator():
        update_versions(
            versions=result.versions, current_key="elected", new_key="is_winner"
        )
        result.save()


class Migration(migrations.Migration):

    dependencies = [("uk_results", "0053_auto_20210928_1007")]

    operations = [migrations.RunPython(code=forwards, reverse_code=backwards)]
