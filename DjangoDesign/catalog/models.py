# модель пользователя.
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import datetime


# создание модели катигорий
class Category(models.Model):
    # поле типа AutoField, которое является первичным ключом и уникальным идентификатором для каждой записи категории
    id = models.AutoField(primary_key=True, unique=True, verbose_name='id')
    # поле типа CharField, которое представляет имя категории
    # max длина 30 символов,должно быть уникальным и имеет значение по умолчанию "Эскиз"
    name = models.CharField(max_length=30, unique=True, default='Эскиз',
                            help_text='Категории',  # текст справки, отображаемое при создании формы
                            verbose_name='Категории',  # текст справки, отображаемое при создании формы
                            # сообщение об ошибке, которое будет отображаться, если значение не уникально
                            error_messages={'unique': "Такая категория уже существует!"})

    class Meta:
        #  метаданные модели, название и множественное число
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    # определяет строковое представление объекта категории, которое будет отображаться при его выводе
    def __str__(self):
        # В данном случае, оно будет равно значению поля name
        return self.name

# создание модели заявки
class Design(models.Model):
    # поле типа AutoField, которое является первичным ключом и уникальным идентификатором для каждой записи заявки
    id = models.AutoField(primary_key=True, unique=True, verbose_name='id')
    # поле типа CharField, которое представляет название заявки
    # max длина 30 символов,должно быть уникальным и имеет значение по умолчанию "Эскиз"
    name = models.CharField(max_length=30, unique=True, help_text='название',
                            verbose_name='Название',
                            error_messages={'unique': "Такая заявка уже существует!"})
    # поле типа CharField, которое представляет описание заявки
    # max длина 50 символов и может быть пустым
    info = models.CharField(max_length=50, help_text='Введите описание', verbose_name='Описание',
                            null=True)
    #  поле типа ImageField, которое представляет изображение, связанное с заявкой
    #  оно должно быть загружено в папку "images/" и не может быть пустым
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', null=False,
                              blank=False)
    #  поле типа DateField, которое представляет дату создания заявки
    #  оно имеет значение по умолчанию - текущую дату
    date = models.DateField(default=datetime.today(), null=True, verbose_name='Дата')
    # поле типа ForeignKey, которое связывает заявку с пользователем
    # оно может быть пустым и ссылается на поле id модели User
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь',
                             null=True, blank=True,
                             to_field='id')
    # поле типа TextField, которое представляет комментарий к заявке
    # оно имеет максимальную длину 400 символов и не может быть пустым
    # blank=False определяет, будет ли поле обязательным в формах
    comment = models.TextField(max_length=400, verbose_name='Комментарий', null=False, blank=False)
    # поле типа ForeignKey, которое связывает заявку с категорией
    # оно может быть пустым и ссылается на модель Category
    # on_delete=models.CASCADE = если категория поста будет удалена, то удалятся и посты
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True,
                                 verbose_name='Категории')
    NEW = 'new'
    LOAD = 'load'
    READY = 'ready'
    LOAN_STATUS = (
        (NEW, 'Новая'),
        (LOAD, 'Принято в работу'),
        (READY, 'Выполнено'),
    )
    # поле типа CharField, которое представляет статус заявки
    # оно имеет максимальную длину 30 символов и имеет предопределенные значения из списка LOAN_STATUS
    # по умолчанию, статус будет равен "new".

    status = models.CharField(max_length=30, choices=LOAN_STATUS, default='new', help_text='Статус',
                              verbose_name='Статус')

    class Meta:
        #  метаданные модели, название и множественное число
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'

    # определяет строковое представление объекта категории, которое будет отображаться при его выводе
    def __str__(self):
        # В данном случае, оно будет равно значению поля name
        return self.name
