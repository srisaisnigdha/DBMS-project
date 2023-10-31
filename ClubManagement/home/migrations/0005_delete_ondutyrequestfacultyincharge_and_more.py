# Generated by Django 4.2.5 on 2023-10-18 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_ondutyrequest_ondutyrequestfacultyincharge_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="OnDutyRequestFacultyIncharge",
        ),
        migrations.DeleteModel(
            name="OnDutyRequestSC",
        ),
        migrations.AlterField(
            model_name="ondutyrequest",
            name="type_of_club",
            field=models.CharField(
                choices=[
                    ("cultural", "cultural"),
                    ("technical", "technical"),
                    ("sports", "sports"),
                ],
                max_length=122,
            ),
        ),
    ]