# Generated by Django 4.1.5 on 2023-01-11 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoopStudio_Backend', '0002_snippet_delete_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
