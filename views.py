from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView

from NeuralPainter.forms import RegisterForm
from NeuralPainter.models import Painter, Paint, Genre
from NeuralPainter.utils import send_email_to_user
import logging

logger = logging.getLogger('django')


class TemplateBasedMixin:
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logger.info('Using user based template')
            self.get_context_data = self.get_context_data_user_template_based
        else:
            logger.info('Using main based template')
            self.get_context_data = self.get_context_data_main_template_based
        return super().get(request, *args, **kwargs)

    def get_context_data_main_template_based(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['based_template_name'] = 'NeuralPainter/main.html'
        return context

    def get_context_data_user_template_based(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['based_template_name'] = 'NeuralPainter/user_templates/user_base.html'
        return context


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'NeuralPainter/register.html'
    success_url = 'login'

    def get_success_url(self, *args, **kwargs):
        logger.info('Sending verification email to user')
        send_email_to_user(self.request, self.object.profile)
        return reverse(self.success_url)


class HomeView(TemplateBasedMixin, TemplateView):
    template_name = 'NeuralPainter/main.html'


class AboutView(TemplateBasedMixin, TemplateView):
    template_name = 'NeuralPainter/about.html'


class PaintersView(TemplateBasedMixin, ListView):
    template_name = 'NeuralPainter/painters.html'
    model = Painter
    queryset = Painter.objects.filter(is_approved=True).all()


class PaintsView(TemplateBasedMixin, ListView):
    template_name = 'NeuralPainter/paints.html'
    model = Paint
    queryset = Paint.objects.filter(is_approved=True).all()


class GenresView(TemplateBasedMixin, ListView):
    template_name = 'NeuralPainter/genres.html'
    model = Genre
    queryset = Genre.objects.filter(is_approved=True).all()
