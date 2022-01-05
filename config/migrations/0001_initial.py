# Generated by Django 4.0 on 2022-01-05 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=350)),
                ('message', models.TextField()),
                ('created', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
