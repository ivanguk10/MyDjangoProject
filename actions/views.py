from logging import getLogger

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from NeuralPainter.utils import NoPhotoException

logger = getLogger('django')


@login_required
def add_to_favorite_paint(request):
    paint_id = request.GET.get('paint_id', None)

    if paint_id is not None:
        success = not request.user.profile.favorite_paints.filter(pk=paint_id).exists()
        if success:
            request.user.profile.add_to_favorite_paint(paint_id)
        else:
            logger.error('Paint already is favorite')
    else:
        success = False
        logger.error('Paint not found')

    data = {'success': success}
    return JsonResponse(data)


@login_required
def add_to_favorite_painter(request):
    painter_id = request.GET.get('painter_id', None)

    if painter_id is not None:
        success = not request.user.profile.favorite_painters.filter(pk=painter_id).exists()

        if success:
            request.user.profile.add_to_favorite_painter(painter_id)
        else:
            logger.error('Painter already is favorite')
    else:
        success = False
        logger.error('Painter not found')

    data = {'success': success}
    return JsonResponse(data)


@login_required
def remove_from_favorite_paint(request):
    paint_id = request.GET.get('paint_id', None)

    if paint_id is not None:
        success = request.user.profile.favorite_paints.filter(pk=paint_id).exists()

        if success:
            request.user.profile.remove_from_favorite_paint(paint_id)
        else:
            logger.error('Paint are not favorite')
    else:
        success = False
        logger.error('Paint not found')
    data = {'success': success}
    return JsonResponse(data)


@login_required
def remove_from_favorite_painter(request):
    painter_id = request.GET.get('painter_id', None)

    if painter_id is not None:
        success = request.user.profile.favorite_painters.filter(pk=painter_id).exists()
        if success:
            request.user.profile.remove_from_favorite_painter(painter_id)
        else:
            logger.error('Painter are not favorite')
    else:
        success = False
        logger.error('Painter not found')
    data = {'success': success}
    return JsonResponse(data)


@login_required
def delete_photo(request):
    deleted_photo_id = request.GET.get('deleted_photo_id', None)
    success = False

    if deleted_photo_id is not None:
        try:
            request.user.profile.delete_photo(deleted_photo_id)
            success = True
        except NoPhotoException:
            success = False
    data = {'success': success}
    return JsonResponse(data)


@login_required
def delete_stylized_photo(request):
    delete_stylized_photo_id = request.GET.get('deleted_stylized_photo_id', None)
    success = False

    print(delete_stylized_photo_id)
    if delete_stylized_photo_id is not None:
        try:
            request.user.profile.delete_stylized_photo(delete_stylized_photo_id)
            success = True
        except NoPhotoException:
            success = False
    data = {'success': success}
    return JsonResponse(data)