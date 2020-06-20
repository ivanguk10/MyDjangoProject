from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django_select2.forms import ModelSelect2Widget

from NeuralPainter.models import Photo, StylizedPhoto, Painter, Paint, Genre


class StylizedPhotoForm(ModelForm):
    class Meta:
        model = StylizedPhoto
        fields = ('paint', 'based_photo')
        widgets = {
            'paint': ModelSelect2Widget(model=Paint, queryset=Paint.objects.filter(is_approved=True),
                                        search_fields=['name__contains'],),
            'based_photo': ModelSelect2Widget(model=Photo, search_fields=['name__contains']),
        }


class PainterForm(ModelForm):
    class Meta:
        model = Painter
        fields = ('name', 'photo', 'biography', 'genres', 'death_date', 'birth_date')

        widgets = {
            'genres': ModelSelect2Widget(model=Genre, queryset=Genre.objects.filter(is_approved=True),
                                         search_fields=['name__contains'], ),
        }

    def clean(self):
        super().clean()
        death_date = self.cleaned_data.get('death_date')
        birth_date = self.cleaned_data.get('birth_date')
        print(type(birth_date))
        if death_date < birth_date:
            raise ValidationError('Death date is bigger than birth date')


class PaintForm(ModelForm):
    class Meta:
        model = Paint
        fields = ('paint', 'painter', 'genre')
        widgets = {
            'painter': ModelSelect2Widget(model=Painter, queryset=Painter.objects.filter(is_approved=True),
                                          search_fields=['name__contains'],),
            'genre': ModelSelect2Widget(model=Genre, queryset=Genre.objects.filter(is_approved=True),
                                        search_fields=['name__contains'],),
        }


