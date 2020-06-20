from logging import getLogger

from django.contrib.auth.models import User
from django.forms import ImageField, EmailField, CharField
from django.contrib.auth.forms import UserCreationForm

from NeuralPainter.models import Profile

logger = getLogger('django')


class RegisterForm(UserCreationForm):
    avatar = ImageField(required=False)
    email = EmailField(required=True, label='Email address')
    first_name = CharField(required=True, label='First name')
    last_name = CharField(required=True, label='Second name')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'last_name', 'first_name', 'password1', 'password2',  'avatar', )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')

        avatar = self.cleaned_data.get('avatar')
        if avatar is not None:
            user.profile = Profile(avatar)
            logger.info('Added avatar to user profile')
        if commit:
            user.save()
        return user
