# Generated by Django 4.1.5 on 2023-07-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meu_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TesteBd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
    ]