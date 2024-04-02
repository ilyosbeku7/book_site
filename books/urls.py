from django.urls import path
from .views import BooksView, AboutView, AddComment
from . import views

app_name='books'

urlpatterns=[
    path('', BooksView.as_view(), name='home_page' ),
    path('about_page/<int:id>', AboutView.as_view(), name='about_page' ),
    path('add_comment/<int:id>', AddComment.as_view(), name='add_comment' ),
    path('category/<int:id>/', views.category, name='category'),
    ]