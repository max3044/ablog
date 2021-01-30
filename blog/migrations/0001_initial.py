# Generated by Django 3.1.5 on 2021-01-29 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.ImageField(upload_to='post_image/')),
                ('post_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('post_text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
