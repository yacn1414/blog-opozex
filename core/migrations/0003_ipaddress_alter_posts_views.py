# Generated by Django 4.2 on 2023-11-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_categories_options_alter_posts_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ips', models.GenericIPAddressField()),
            ],
            options={
                'verbose_name': 'ip',
                'verbose_name_plural': 'ips',
            },
        ),
        migrations.AlterField(
            model_name='posts',
            name='views',
            field=models.IntegerField(max_length=255),
        ),
    ]