from logging import getLogger

from django.views.generic import DetailView
from NeuralPainter.models import Paint, Painter, Photo, StylizedPhoto, Genre
from NeuralPainter.views import TemplateBasedMixin

logger = getLogger('django')


class PaintView(TemplateBasedMixin, DetailView):
    template_name = 'NeuralPainter/detailed_templates/paint.html'
    model = Paint


class PainterView(TemplateBasedMixin, DetailView):
    template_name = 'NeuralPainter/detailed_templates/painter.html'
    model = Painter


class GenreView(TemplateBasedMixin, DetailView):
    template_name = 'NeuralPainter/detailed_templates/genre.html'
    model = Genre


class PhotoView(TemplateBasedMixin, DetailView):
    template_name = 'NeuralPainter/detailed_templates/photo.html'
    model = Photo


class StylizedPhotoView(TemplateBasedMixin, DetailView):
    template_name = 'NeuralPainter/detailed_templates/stylized_photo.html'
    model = StylizedPhoto
