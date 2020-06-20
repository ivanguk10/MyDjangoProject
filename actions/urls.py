from django.urls import path

from NeuralPainter.actions.views import add_to_favorite_paint, add_to_favorite_painter, \
    remove_from_favorite_painter, remove_from_favorite_paint, delete_stylized_photo, delete_photo

urlpatterns = [
    path('remove_favorite_painter', remove_from_favorite_painter, name='remove_favorite_painter'),
    path('remove_favorite_paint', remove_from_favorite_paint, name='remove_favorite_paint'),

    path('add_favorite_painter', add_to_favorite_painter, name='add_favorite_painter'),
    path('add_favorite_paint', add_to_favorite_paint, name='add_favorite_paint'),

    path('delete_stylized_photo', delete_stylized_photo, name='delete_stylized_photo'),
    path('delete_photo', delete_photo, name='delete_photo')
]
