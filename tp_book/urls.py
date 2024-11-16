from django.urls import path
from . import views

urlpatterns = [
    path ('', views.book_view ),
    path('<int:book_id>', views.book_detail_view),
]