# Generated by Django 5.1.1 on 2024-09-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FruitFaq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=200)),
                ('faq', models.CharField(max_length=1000)),
                ('img_url', models.CharField(max_length=150)),
            ],
        ),
    ]
