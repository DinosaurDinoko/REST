# импорт класса AppConfig из модуля django.apps, который позволяет настроить конфигурацию приложения Django.
from django.apps import AppConfig


# Этот класс будет использоваться для конфигурации приложения catalog.
class CatalogConfig(AppConfig):
    # указание типа автоматического поля для моделей в приложении. В данном случае, используется тип BigAutoField,
    # который поддерживает большие целочисленные значения для автоинкрементного поля.
    default_auto_field = 'django.db.models.BigAutoField'
    # указание имени приложения.
    name = 'catalog'
