# Generated by Django 4.2 on 2023-10-11 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.CharField(max_length=255)),
                ('subject_name', models.CharField(max_length=255)),
                ('topic_name', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('level', models.CharField(max_length=255)),
                ('q1', models.IntegerField()),
                ('q2', models.IntegerField()),
                ('q3', models.IntegerField()),
                ('q4', models.IntegerField()),
                ('q5', models.IntegerField()),
                ('a1', models.IntegerField()),
                ('a2', models.IntegerField()),
                ('a3', models.IntegerField()),
                ('a4', models.IntegerField()),
                ('a5', models.IntegerField()),
            ],
        ),
    ]
