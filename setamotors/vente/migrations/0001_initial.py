# Generated by Django 4.1.7 on 2023-03-11 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_add', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_add'],
            },
        ),
        migrations.CreateModel(
            name='vehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immatriculation', models.CharField(max_length=500)),
                ('mark', models.CharField(max_length=255)),
                ('describe', models.TextField()),
                ('image', models.CharField(max_length=5000)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='vente.category')),
            ],
            options={
                'ordering': ['-date_add'],
            },
        ),
    ]
