from django.contrib import admin
from NeuralPainter.models import Profile, Painter, Paint, Photo, StylizedPhoto, Genre
from NeuralPainter.admin_actions import send_email_to_users, mark_approved


# Register your models here.


@admin.register(Paint)
class PaintAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', )
    actions = [mark_approved]


@admin.register(Painter)
class PainterAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    actions = [mark_approved]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    actions = [mark_approved]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('verified',)
    actions = [send_email_to_users]


admin.site.register(Photo)
admin.site.register(StylizedPhoto)
