from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('news/', views.news_list, name='news_list'),
    path('add/', views.add_news, name='add_news'),
    path('edit/<int:id>/', views.edit_news, name='edit_news'),
    path('delete/<int:id>/', views.delete_news, name='delete_news'),
    path('', views.index, name='index'),
    path('add_author/', views.add_author, name="add_author"),
    path('add_category/', views.add_category, name='add_category'),
    path('add_publisher', views.add_publisher, name='add_publisher'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)