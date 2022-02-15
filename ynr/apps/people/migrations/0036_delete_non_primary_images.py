# Generated by Django 3.2.4 on 2022-02-15 10:51

from django.db import migrations


def delete_non_primary_images(apps, schema_editor):
    PersonImage = apps.get_model("people", "PersonImage")
    PersonImage.objects.filter(is_primary=False).delete()


class Migration(migrations.Migration):

    dependencies = [("people", "0035_alter_person_birth_date")]

    operations = [
        migrations.RunPython(
            code=delete_non_primary_images,
            reverse_code=migrations.RunPython.noop,
        )
    ]
