# импорт настроек проекта
from django.conf import settings
# импорт функции для добавления статических файлов
from django.conf.urls.static import static
# импорт модуля административной панели Django
from django.contrib import admin
# импорт функций для определения URL-путей и включения других URL-конфигураций
from django.urls import path, include
# импорт класса для перенаправления запросов
from django.views.generic import RedirectView

urlpatterns = [
    #  URL-путь для подключения URL-конфигурации приложения "catalog"
    path('catalog/', include('catalog.urls')),
    #  URL-путь для перенаправления с корневого URL на "catalog/"
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
    #  URL-путь для подключения административной панели Django
    path('admin/', admin.site.urls),
    # URL-путь для подключения URL-конфигурации аутентификации Django
    path('accounts/', include('django.contrib.auth.urls')),
]
# URL-путь для обслуживания статических файлов, если проект находится в режиме отладки
if settings.DEBUG:
    # обавление URL-пути для обслуживания статических файлов из директории
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

