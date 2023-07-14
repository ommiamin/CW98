from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('detail/<int:Post_id>' , views.detail , name='details'),
    path('delete/<int:post_id>', views.delete , name='delete'),
    path('post_list/', views.post_list , name='post_list'),
    path('authors/', views.author_list , name='author_list'),
    path('author/<int:Author_id>', views.author , name='authors'),
    path('category/', views.category_list , name='category_list'),
    path('category/<int:Author_id>', views.category , name='category'),

]
