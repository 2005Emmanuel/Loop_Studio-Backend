# Generated by Django 4.1.5 on 2023-01-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoopStudio_Backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('code', models.TextField()),
                ('linenos', models.BooleanField(default=False)),
                ('language', models.CharField(default='python', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='clients',
        ),
    ]