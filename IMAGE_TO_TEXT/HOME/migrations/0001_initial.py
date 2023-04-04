# Generated by Django 4.1.7 on 2023-03-24 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uploads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Images', models.ImageField(upload_to='media')),
                ('Texts', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'UPLOAD',
            },
        ),
    ]