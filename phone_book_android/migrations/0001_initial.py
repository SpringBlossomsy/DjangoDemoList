# Generated by Django 2.1.11 on 2019-12-04 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('modify_time', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='phone_book_android/phone_image/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
