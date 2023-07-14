from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('detail/<int:Post_id>' , views.detail , name='details'),
    path('delete/<int:post_id/', views.delete , name='delete')
]
