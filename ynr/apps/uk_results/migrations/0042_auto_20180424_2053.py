# Generated by Django 1.9.13 on 2018-04-24 19:53


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("uk_results", "0041_auto_20180424_2049")]

    operations = [
        migrations.AlterModelOptions(
            name="resultset",
            options={
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
            },
        ),
        migrations.RemoveField(model_name="candidateresult", name="source"),
        migrations.RemoveField(model_name="resultset", name="review_source"),
        migrations.RemoveField(model_name="resultset", name="reviewed_by"),
    ]
