# Generated by Django 2.2.4 on 2019-11-13 17:29

from django.db import migrations, models
import moderation_queue.models


class Migration(migrations.Migration):

    dependencies = [
        ("moderation_queue", "0028_positive_int_field_update_existing")
    ]

    operations = [
        migrations.AlterField(
            model_name="queuedimage",
            name="image",
            field=models.ImageField(
                max_length=512,
                upload_to=moderation_queue.models.queued_image_filename,
            ),
        )
    ]
