from django.urls import path
from NeuralPainter.detailed_pages.views import PaintView, PainterView, GenreView, PhotoView, StylizedPhotoView

urlpatterns = [
    path('paint/<slug:slug>', PaintView.as_view(), name='paint'),
    path('painter/<slug:slug>', PainterView.as_view(), name='painter'),
    path('genre/<slug:slug>', GenreView.as_view(), name='genre'),
    path('photo/<slug:slug>', PhotoView.as_view(), name='photo'),
    path('stylized_photo/<int:pk>', StylizedPhotoView.as_view(), name='stylized_photo'),
]