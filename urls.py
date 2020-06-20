"""NeuralPainterProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from NeuralPainter.views import HomeView, RegisterView, PaintersView, PaintsView, GenresView, AboutView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('painters/', PaintersView.as_view(), name='painters'),
    path('paints/', PaintsView.as_view(), name='paints'),
    path('genres/', GenresView.as_view(), name='genres'),
    path('about/', AboutView.as_view(), name='about'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='NeuralPainter/login.html'), name='login'),

    path('content/', include('NeuralPainter.detailed_pages.urls')),


    path('user/', include('NeuralPainter.user_pages.urls')),
    path('user/actions/', include('NeuralPainter.actions.urls')),
    path('user/content/', include('NeuralPainter.user_detailed_pages.urls')),
    path('user/content/add/', include('NeuralPainter.add_pages.urls')),


    path('admin/', admin.site.urls),
    path('select2/', include('django_select2.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
