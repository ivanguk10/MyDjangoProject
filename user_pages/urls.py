from django.contrib.auth.views import LogoutView
from django.urls import path

from NeuralPainter.user_pages import views

urlpatterns = [
    path(r'', views.user_view, name='user'),
    path(r'logout', LogoutView.as_view(template_name='NeuralPainter/logout.html'), name='logout'),
    path(r'favorite_paints', views.UserFavoritePaintsView.as_view(), name='favorite_paints'),
    path(r'favorite_painters', views.UserFavoritePaintersView.as_view(), name='favorite_painters'),
    path(r'photos', views.UserPhotosView.as_view(), name='photos'),
    path(r'stylized_photos', views.UserStylizedPhotosView.as_view(), name='stylized_photos'),
    path(r'activate/<str:uid>/<str:token>', views.ActivateUser.as_view(), name='activate')
]
