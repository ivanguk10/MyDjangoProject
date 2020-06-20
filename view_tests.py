from django.test import Client
from django.urls import reverse

from NeuralPainter.views import HomeView
from NeuralPainter.tests.model_tests import user_factory


import pytest


@pytest.mark.parametrize('username, password, logged_username, logged_password, site_version', [
    ('vanya', '123456789', 'vanya', '123456789', 'NeuralPainter/user_templates/user_base.html'),
    ('vanya', '123456789', 'vanya', '12345678', 'NeuralPainter/main.html')
])
@pytest.mark.django_db(transaction=True)
def test_template_based_mixin(user_factory, username, password, logged_username, logged_password, site_version):
    user = user_factory(username=username)
    user.set_password(password)
    user.save()

    client = Client()
    client.login(username=logged_username, password=logged_password)
    response = client.get(reverse('about'))

    assert response.context['based_template_name'] == site_version

