from django.urls import path, include
from . import views
from rest_framework import routers

r1 = routers.DefaultRouter()
r1.register('blogs',views.BlogViewSet)
r1.register('users',views.UserViewSet)
urlpatterns = [

    path('',views.BlogListView.as_view()),
    path('<int:pk>/',views.BlogDetailView.as_view()),
    path('users/',views.UserList.as_view()),
    path('user/<int:pk>/',views.UserDetail.as_view()),
    path('viewsets/', include(r1.urls)),
    
    

]