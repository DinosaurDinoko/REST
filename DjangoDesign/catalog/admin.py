# импорт модуля административной панели Django.
from django.contrib import admin
# мпорт моделей Design и Category из приложения.
from .models import Design, Category

# регистрация модели Design в административной панели.
# Это позволяет администраторам сайта управлять объектами этой модели через административный интерфейс.
admin.site.register(Design)

# регистрация модели Category в административной панели.
admin.site.register(Category)