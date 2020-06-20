from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from NeuralPainter.models import Photo, StylizedPhoto


class UserPhotoView(LoginRequiredMixin, DetailView):
    template_name = 'NeuralPainter/detailed_templates/photo.html'
    model = Photo


class UserStylizedPhotoView(LoginRequiredMixin, DetailView):
    template_name = 'NeuralPainter/detailed_templates/stylized_photo.html'
    model = StylizedPhoto
