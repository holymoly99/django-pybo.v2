# Generated by Django 4.1.7 on 2023-03-02 07:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pybo", "0006_answer_voter_question_voter_alter_answer_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="voter",
            field=models.ManyToManyField(
                related_name="voter_answer", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="voter",
            field=models.ManyToManyField(
                related_name="voter_question", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]