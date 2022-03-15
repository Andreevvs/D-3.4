from django.urls import path
from .views import NewsList, NewsDetail

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
]