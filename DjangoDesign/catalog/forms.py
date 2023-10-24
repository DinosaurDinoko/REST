# содержит классы для создания и обработки форм.
from django import forms
# модель пользователя.
from django.contrib.auth.models import User
# исключение, возникающее при неверном значении поля формы.
from django.core.exceptions import ValidationError
# валидаторы для проверки правильности ввода электронной почты
from django.core.validators import EmailValidator, RegexValidator
#  модели данных для дизайна и категорий
from .models import Design, Category


# создания формы регистрации пользователя
class UserRegistrationForm(forms.ModelForm):
    # формв логина
    username = forms.CharField(label='Логин', widget=forms.TextInput,
                               validators=[RegexValidator(r'[a-zA-Z\-]',
                                                          'доступны'
                                                          'только латинские'
                                                          'символы')],
                               required=True)

    full_name = forms.CharField(label='ФИО', widget=forms.TextInput,
                                validators=
                                [RegexValidator(r'[а-яА-ЯёЁ\-\s]',

                                                'В ФИО доступна только кириллица, пробелы и дефис')],
                                required=True)

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput, required=True)
    email = forms.EmailField(label='Email', widget=forms.EmailInput, required=True,
                             validators=[EmailValidator('Email не верен')])
    checkbox = forms.CharField(label='Согласие на обработку персональных данных',
                               widget=forms.CheckboxInput,
                               required=True)

    class Meta:
        model = User  # указание модели, для которой создается фильтр.
        fields = ('username', 'email', 'full_name')  # список полей модели, которые должны быть отображены в форме

    # методы выполняют проверку введенных данных для полей
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            # Если данные не проходят проверку, генерируется исключение
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

    # проверяет, что поле checkbox было отмечено (значение равно True) и генерирует исключение, если это не так.
    def clean_checkbox(self):
        cd = self.cleaned_data
        print(cd['checkbox'])
        if not cd['checkbox']:
            raise forms.ValidationError('Подтвердите обработку персональных данных')
        return cd['checkbox']


# форма записи.
class PostForm(forms.ModelForm):
    # выполняет проверку загружаемого изображения
    def clean_image(self):
        # Метод получает значение поля image из очищенных данных формы
        image = self.cleaned_data.get('image')
        if image:
            # Если значение существует, то проверяется его размер.
            if image.size > 2 * 1024 * 1024:
                # Если размер превышает 2 мегабайта, генерируется исключение
                raise ValidationError("Вес картинки больше 2мб")
            return image
        else:
            # В противном случае, метод возвращает значение поля image.
            raise ValidationError("Не возможно обработать картинку")

    class Meta:  # определяет модель данных, с которой связана форма
        model = Design
        fields = ['name', 'info', 'image', 'category']  # список полей модели, которые должны быть отображены в форме


# форма создания записи
class PostFormUpdateNew(forms.ModelForm):
    # выполняет проверку загружаемого изображения

    def clean_image(self):
        # Метод получает значение поля image из очищенных данных формы
        image = self.cleaned_data.get('image')
        if image:
            # Если значение существует, то проверяется его размер.
            if image.size > 2 * 1024 * 1024:
                # Если размер превышает 2 мегабайта, генерируется исключение
                raise ValidationError("Вес картинки больше 2мб")
            return image
        else:
            # В противном случае, метод возвращает значение поля image.
            raise ValidationError("Не возможно обработать картинку")

    class Meta:
        model = Design  # определяет модель данных, с которой связана форма
        fields = ['status', 'category']  # список полей модели, которые должны быть отображены в форме


# форма обновления записи
class PostFormUpdateReady(forms.ModelForm):
    # выполняет проверку загружаемого изображения

    def clean_image(self):
        # Метод получает значение поля image из очищенных данных формы
        image = self.cleaned_data.get('image')
        if image:
            # Если значение существует, то проверяется его размер.
            if image.size > 2 * 1024 * 1024:
                # Если размер превышает 2 мегабайта, генерируется исключение
                raise ValidationError("Вес картинки больше 2мб")
            return image
        else:
            # В противном случае, метод возвращает значение поля image.
            raise ValidationError("Не возможно обработать картинку")

    class Meta:
        model = Design  # определяет модель данных, с которой связана форма
        fields = ['image', 'comment', 'status']  # список полей модели, которые должны быть отображены в форме


# класс формы позволяет создавать и обновлять записи о категориях с отображением соответствующих полей модели данных.
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
