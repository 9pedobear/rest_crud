from django.urls import path
from .views import ArticleCreateView, ArticleListView, ArticleRetriveView

urlpatterns = [
    path('article/create/', ArticleCreateView.as_view()),
    path('article/list/', ArticleListView.as_view()),
    path('article/retrive/<int:pk>', ArticleRetriveView.as_view()),
]

