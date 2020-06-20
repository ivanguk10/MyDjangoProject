from django.urls import path

from NeuralPainter.add_pages.views import AddPainter, AddPaint, AddGenre, AddPhoto, AddStylizedPhoto

urlpatterns = [
    path('painter', AddPainter.as_view(), name='add_painter'),
    path('paint', AddPaint.as_view(), name='add_paint'),
    path('genre', AddGenre.as_view(), name='add_genre'),
    path('photo', AddPhoto.as_view(), name='add_photo'),
    path('stylized_photo', AddStylizedPhoto.as_view(), name='add_stylized_photo'),
]

