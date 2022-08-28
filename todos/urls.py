from django.urls import path
from . import views


urlpatterns = [
    path('', views.TodoListgAPIView.as_view()),
    path('<int:pk>/', views.TodoDetailsAPIView.as_view()),
    path('api/<int:id>/', views.TodoListgAPIView.as_view()),
]
