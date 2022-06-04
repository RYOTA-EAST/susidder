from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name='twitter'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)