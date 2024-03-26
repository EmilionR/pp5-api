from django.urls import path
from likes import views

urlpatterns = [
    path('blocks/', views.LikeList.as_view()),
    path('blocks/<int:pk>/', views.LikeDetail.as_view()),
]