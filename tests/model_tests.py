from datetime import datetime
from mock import MagicMock
import pytest

from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.files import File

from NeuralPainter.models import Genre, Painter, Paint, Photo, StylizedPhoto

image_mock = MagicMock(spec=File, name='FileMock')
image_mock.name = 'test.png'


@pytest.fixture
def genre_factory():
    def create_genre(name='Genre', description='Genre description', is_approved=False):

        if not Genre.objects.filter(name=name).exists():
            genre = Genre.objects.create(name=name, description=description, is_approved=is_approved)
            return genre
        else:
            return Genre.objects.filter(name=name).first()

    return create_genre


@pytest.fixture
def painter_factory(genre_factory):
    def create_painter(name='Painter',
                       biography='Painter biography',
                       death_date=datetime.now(),
                       birth_date=datetime.now(),
                       is_approved=False):
        if not Painter.objects.filter(name=name).exists():
            painter = Painter.objects.create(name=name,
                                             photo=image_mock,
                                             biography=biography,
                                             death_date=death_date,
                                             birth_date=birth_date,
                                             is_approved=is_approved)
            painter.genres.add(genre_factory())
            return painter
        else:
            return Painter.objects.filter(name=name).first()

    return create_painter


@pytest.fixture
def paint_factory(genre_factory, painter_factory):
    def create_paint(name='Paint', is_approved=False):
        if not Paint.objects.filter(name=name).exists():
            paint = Paint.objects.create(name=name,
                                         paint=image_mock,
                                         genre=genre_factory(),
                                         painter=painter_factory(),
                                         is_approved=is_approved)
            return paint
        else:
            return Paint.objects.filter(name=name).first()

    return create_paint


@pytest.fixture
def user_factory():
    def create_user(username='User',
                    password='password',
                    email='email',
                    first_name='firstname',
                    last_name='lastname'):
        if not User.objects.filter(username=username).exists():
            user = User.objects.create(username=username,
                                       email=email,
                                       password=password,
                                       first_name=first_name,
                                       last_name=last_name)
            return user
        else:
            return User.objects.filter(username=username).first()

    return create_user


@pytest.fixture
def profile_factory(user_factory):
    def create_profile(verified=False):
        user = user_factory()
        user.profile.avatar = image_mock
        user.profile.verified = verified
        user.save()

        return user.profile

    return create_profile


@pytest.fixture
@pytest.mark.django_db
def photo_factory(profile_factory):
    def create_photo(name='Photo'):
        if not Photo.objects.filter(name=name).exists():
            photo = Photo.objects.create(name=name,
                                         user=profile_factory(),
                                         photo=image_mock)
            return photo
        else:
            return Photo.objects.filter(name=name).first()

    return create_photo


@pytest.fixture
def stylized_photo_factory(photo_factory, paint_factory):
    def create_styled_photo(based_photo_name, paint_name):
        return StylizedPhoto.objects.create(based_photo=photo_factory(name=based_photo_name),
                                            paint=paint_factory(name=paint_name),
                                            is_stylized=True)

    return create_styled_photo


@pytest.mark.django_db
def test_slug(paint_factory):
    name = 'Paint'
    assert paint_factory(name=name).slug == slugify(name)


@pytest.mark.django_db
def test_genre_str(genre_factory):
    name = 'Cubism'
    assert str(genre_factory(name=name)) == 'Genre {}'.format(name)


@pytest.mark.django_db
def test_paint_str(paint_factory):
    name = 'Creation of Adam'
    assert str(paint_factory(name=name)) == 'Paint {}'.format(name)


@pytest.mark.django_db
def test_painter_str(painter_factory):
    name = 'Leonardo'
    assert str(painter_factory(name=name)) == 'Painter {}'.format(name)


@pytest.mark.django_db
def test_stylized_photo_str(stylized_photo_factory):
    based_photo_name = 'My school photo'
    paint_name = 'Van Gogh'
    assert str(stylized_photo_factory
               (based_photo_name=based_photo_name,
                paint_name=paint_name)) == 'Stylized {} by {}'.format(based_photo_name, paint_name)


@pytest.mark.django_db
def test_photo_str(photo_factory):
    name = 'MyPhoto'
    assert str(photo_factory(name=name)) == 'Photo {}'.format(name)


@pytest.mark.django_db
def test_add_to_favorite_paint(profile_factory, paint_factory):
    profile = profile_factory()

    paint_mona_lisa = paint_factory(name='Mona Lisa')
    paint_black_square = paint_factory(name='Black square')

    profile.add_to_favorite_paint(paint_mona_lisa.id)

    assert profile.favorite_paints.filter(pk=paint_mona_lisa.id).exists()
    assert not profile.favorite_paints.filter(pk=paint_black_square.id).exists()


@pytest.mark.django_db
def test_add_to_favorite_painter(profile_factory, painter_factory):
    profile = profile_factory()

    painter_mark_shagal = painter_factory(name='Mark Shagal')
    painter_ilya_repin = painter_factory(name='Ilya Repin')

    profile.add_to_favorite_painter(painter_mark_shagal.id)

    assert profile.favorite_painters.filter(pk=painter_mark_shagal.id).exists()
    assert not profile.favorite_painters.filter(pk=painter_ilya_repin.id).exists()


@pytest.mark.django_db
def test_remove_from_favorite_paint(profile_factory, paint_factory):
    profile = profile_factory()

    paint_the_scream = paint_factory(name='The Scream')
    paint_sunflower = paint_factory(name='Sunflower')

    profile.favorite_paints.add(paint_the_scream)
    profile.favorite_paints.add(paint_sunflower)

    profile.remove_from_favorite_paint(paint_the_scream.id)

    assert profile.favorite_paints.filter(pk=paint_sunflower.id).exists()
    assert not profile.favorite_paints.filter(pk=paint_the_scream.id).exists()


@pytest.mark.django_db
def test_remove_from_favorite_painter(profile_factory, painter_factory):
    profile = profile_factory()

    painter_delacroix = painter_factory(name='Delacroix')
    painter_manet = painter_factory(name='Manet')

    profile.favorite_painters.add(painter_delacroix)
    profile.favorite_painters.add(painter_manet)

    profile.remove_from_favorite_painter(painter_delacroix.id)

    assert profile.favorite_painters.filter(pk=painter_manet.id).exists()
    assert not profile.favorite_painters.filter(pk=painter_delacroix.id).exists()
