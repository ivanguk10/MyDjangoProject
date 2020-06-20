from django.urls import path
from NeuralPainter.user_detailed_pages.views import UserPhotoView, UserStylizedPhotoView

urlpatterns = [
    path('photo/<str:slug>', UserPhotoView.as_view(), name='user_photo'),
    path('stylized_photo/<int:pk>', UserStylizedPhotoView.as_view(), name='user_stylized_photo'),
]
