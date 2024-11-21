from django.urls import path
from . import views

urlpatterns = [
      # Ensure 'home' is the name of the route
    path('add-farm/',views.addFarm, name='add_farm'),
    path('register/', views.register, name='register'),
    path('upload-media/', views.uploadMedia, name='upload_media'),
    path('notifications/', views.notifications,name='notifications'),

]