from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from PIL import Image

import numpy as np


def send_email_to_user(request, profile):
    current_site = get_current_site(request)
    email_subject = 'Activate Your Account'

    message = render_to_string('NeuralPainter/user_templates/verification_email.html', {
        'user': profile.user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(profile.user.id)),
        'token': default_token_generator.make_token(profile.user),
    })

    to_email = profile.user.email
    email = EmailMessage(email_subject, message, to=[to_email])
    email.send()


def get_image_from_array(image_array):
    return Image.fromarray(np.uint8(image_array * 255))


class SingletonMeta(type):
    _instance = None

    def __call__(cls):
        if cls._instance is None:
            cls._instance = super().__call__()
        return cls._instance


class NoPhotoException(Exception):
    pass