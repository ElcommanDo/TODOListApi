from rest_framework import serializers
from .models import Blog
from django.contrib.auth import get_user_model

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = "__all__"



class UserSerializer(serializers.ModelSerializer): # new
    class Meta: 
        model = get_user_model()
        fields = ('id', 'username',)
