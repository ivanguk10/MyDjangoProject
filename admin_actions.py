import logging

from gevent.pool import Pool

from NeuralPainter.utils import send_email_to_user

logger = logging.getLogger('django')


def send_email_to_users(modeladmin, request, queryset):
    class Sender:
        def __init__(self, request):
            self.request = request

        def __call__(self, user):
            send_email_to_user(self.request, user)

    p = Pool(5)
    p.map(Sender(request), queryset)
    logging.info('Sending emails to users')


def mark_approved(modeladmin, request, queryset):
    for not_approved in queryset:
        not_approved.is_approved = True
        not_approved.save()
