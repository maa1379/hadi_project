# Generated by Django 4.0 on 2022-01-05 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('product', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForbiddenWords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11)),
                ('text', models.TextField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('exportal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.exportal')),
                ('internal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.internal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Nemoneh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11)),
                ('text', models.TextField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('exportal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.exportal')),
                ('internal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.internal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Hold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11)),
                ('text', models.TextField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('exportal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.exportal')),
                ('internal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.internal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
