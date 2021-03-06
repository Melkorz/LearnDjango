from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewDetailViews.as_view(), name='news-detail'),  # pk - первичный ключ
    path('<int:pk>/update', views.NewsUpdateViews.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteViews.as_view(), name='news-delete'),
]
