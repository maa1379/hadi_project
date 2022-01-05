# Generated by Django 4.0 on 2022-01-05 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mine', models.CharField(max_length=255)),
                ('kode_sine_kar', models.CharField(max_length=255)),
                ('shomareh_serail_qoleh_dr_madan', models.CharField(max_length=255)),
                ('stone_name', models.CharField(max_length=255)),
                ('created', models.DateField()),
                ('kode_darage_bandi', models.CharField(max_length=255)),
                ('tonazh_taghribi', models.PositiveIntegerField()),
                ('uniqu_id', models.CharField(blank=True, max_length=255, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('line', models.BooleanField(default=False)),
                ('uploder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Exportal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mine', models.CharField(max_length=255)),
                ('kode_sine_kar', models.CharField(max_length=255)),
                ('kode_peleh', models.CharField(max_length=255)),
                ('stone_name', models.CharField(max_length=255)),
                ('created', models.DateField()),
                ('shomareh_serail_qoleh_dr_madan', models.CharField(max_length=255)),
                ('kode_darz', models.CharField(max_length=255)),
                ('kode_ghavareh', models.CharField(max_length=255)),
                ('kode_rang', models.CharField(max_length=255)),
                ('length', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('vazne_taghribi', models.PositiveIntegerField()),
                ('vazne_baskol', models.PositiveIntegerField()),
                ('buyer', models.CharField(max_length=255)),
                ('uniqu_id', models.CharField(blank=True, max_length=255, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('uploder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
            ],
        ),
    ]
