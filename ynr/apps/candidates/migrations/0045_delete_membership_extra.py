# Generated by Django 1.9.13 on 2018-05-21 15:52


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("candidates", "0044_remove_membership_fk_to_election"),
        ("popolo", "0004_move-extra-data-to-base"),
        ("candidates", "0040_membershipextra_post_election"),
    ]

    operations = [migrations.DeleteModel(name="MembershipExtra")]
