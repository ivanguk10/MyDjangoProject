from logging import getLogger

from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from NeuralPainter.models import Paint, Painter, Photo, StylizedPhoto, Profile
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

logger = getLogger('django')


class UserFavoritePaintersView(LoginRequiredMixin, ListView):
    model = Painter
    template_name = 'NeuralPainter/user_templates/user_favorite_painters.html'

    def get_queryset(self):
        super(UserFavoritePaintersView, self).get_queryset()
        queryset = self.request.user.profile.favorite_painters.all()
        logger.info('Got user favorite painters')
        return queryset


class UserFavoritePaintsView(LoginRequiredMixin, ListView):
    model = Paint
    template_name = 'NeuralPainter/user_templates/user_favorite_paints.html'

    def get_queryset(self):
        super(UserFavoritePaintsView, self).get_queryset()
        queryset = self.request.user.profile.favorite_paints.all()
        logger.info('Got user favorite paints')
        return queryset


class UserPhotosView(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'NeuralPainter/user_templates/user_photos.html'

    def get_queryset(self):
        super(UserPhotosView, self).get_queryset()
        queryset = self.request.user.profile.photos.all()
        logger.info('Got user photos')
        return queryset


class UserStylizedPhotosView(LoginRequiredMixin, ListView):
    model = StylizedPhoto
    template_name = 'NeuralPainter/user_templates/user_stylized_photos.html'

    def get_queryset(self):
        super(UserStylizedPhotosView, self).get_queryset()
        queryset = StylizedPhoto.objects.filter(based_photo__user=self.request.user.profile)
        logger.info('Got user stylized photos')
        return queryset


class ActivateUser(TemplateView):
    template_name = 'NeuralPainter/user_templates/verificate_user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        uid = self.kwargs['uid']
        token = self.kwargs['token']

        try:
            id = urlsafe_base64_decode(uid).decode()
            user = User.objects.get(pk=id)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            logger.error('User not found')

        if user is not None and default_token_generator.check_token(user, token):
            user.profile.verified = True
            user.save()
            context['is_success'] = True
            logger.info('User verified')
        else:
            context['is_success'] = False
            logger.error('Link is not valid')
        return context


def user_view(request):
    return redirect('home')
