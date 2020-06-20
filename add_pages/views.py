from logging import getLogger

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from NeuralPainter.add_pages.forms import StylizedPhotoForm, PainterForm, PaintForm
from NeuralPainter.models import Painter, Paint, Genre, Photo, StylizedPhoto, Profile

logger = getLogger('django')


class AddPainter(CreateView, LoginRequiredMixin):
    model = Painter
    form_class = PainterForm
    template_name = 'NeuralPainter/add_templates/painter.html'

    def get_success_url(self):
        return reverse('painters')


class AddPaint(CreateView, LoginRequiredMixin):
    model = Paint
    template_name = 'NeuralPainter/add_templates/paint.html'
    form_class = PaintForm

    def get_success_url(self):
        return reverse('paints')


class AddGenre(CreateView, LoginRequiredMixin):
    model = Genre
    template_name = 'NeuralPainter/add_templates/genre.html'
    fields = ('name', 'description',)

    def get_success_url(self):
        return reverse('genres')


class AddPhoto(CreateView, LoginRequiredMixin):
    model = Photo
    template_name = 'NeuralPainter/add_templates/photo.html'
    fields = ('name', 'photo')

    def get_success_url(self):
        return reverse('photos')

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = Profile.objects.get(user=self.request.user)
        photo.save()
        logger.info('Photo added to user')
        return HttpResponseRedirect(self.get_success_url())


class AddStylizedPhoto(CreateView, LoginRequiredMixin):
    model = StylizedPhoto
    template_name = 'NeuralPainter/add_templates/stylized_photo.html'
    form_class = StylizedPhotoForm

    def get_success_url(self):
        return reverse('stylized_photos')