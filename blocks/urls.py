from django.urls import path
from blocks import views

urlpatterns = [
    path('blocks/', views.BlockList.as_view()),
    path('blocks/<int:pk>/', views.BlockDetail.as_view()),
]
