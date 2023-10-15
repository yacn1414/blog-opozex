# Generated by Django 4.2 on 2023-10-14 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name': 'پست', 'verbose_name_plural': 'پست ها'},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'verbose_name': 'اطلاعات سایت', 'verbose_name_plural': 'اطلاعات سایت'},
        ),
        migrations.AlterModelOptions(
            name='socials',
            options={'verbose_name': 'شبکه مجازی', 'verbose_name_plural': 'شبکه های مجازی'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='t_post',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='posts',
            name='categories',
        ),
        migrations.AlterField(
            model_name='posts',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='posts',
            name='categories',
            field=models.ManyToManyField(to='core.categories'),
        ),
    ]