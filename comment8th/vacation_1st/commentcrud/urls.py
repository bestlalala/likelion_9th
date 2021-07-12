from django.urls import path 
from . import views

urlpatterns = [
    path('commentcreate/<int:post_id>', views.commentcreate, name='commentcreate'),
]