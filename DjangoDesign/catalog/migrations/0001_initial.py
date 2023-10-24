# Generated by Django 3.2 on 2023-10-24 16:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('name', models.CharField(default='Эскиз', error_messages={'unique': 'Такая категория уже существует!'}, help_text='Категории', max_length=30, unique=True, verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('name', models.CharField(error_messages={'unique': 'Такая заявка уже существует!'}, help_text='название', max_length=30, unique=True, verbose_name='Название')),
                ('info', models.CharField(help_text='Введите описание', max_length=50, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Изображение')),
                ('date', models.DateField(default=datetime.datetime(2023, 10, 24, 23, 2, 23, 317603), null=True, verbose_name='Дата')),
                ('comment', models.TextField(max_length=400, verbose_name='Комментарий')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('load', 'Принято в работу'), ('ready', 'Выполнено')], default='new', help_text='Статус', max_length=30, verbose_name='Статус')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категории')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заявку',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
