# Generated by Django 4.1 on 2022-09-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='face_photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_input', models.ImageField(upload_to='images_input/')),
            ],
        ),
        migrations.CreateModel(
            name='predicted_photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_output', models.ImageField(blank=True, default='default.png', null=True, upload_to='images_output/')),
            ],
        ),
    ]