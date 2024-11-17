from django.urls import path
from . import views

urlpatterns = [

    path('user/', views.UserGenericAPIView.as_view() ),
    path('generic/', views.BookGenericAPIView.as_view() ),
    path('generic/<int:pk>', views.BookDetailAPIView.as_view() ),
]