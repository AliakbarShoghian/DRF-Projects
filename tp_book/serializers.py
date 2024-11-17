from rest_framework import serializers
from tp_book.models import Book
from django.contrib.auth import get_user_model
User = get_user_model()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'
