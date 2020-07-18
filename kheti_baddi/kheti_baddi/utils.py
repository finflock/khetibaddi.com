from django.utils.text import slugify
import os, datetime, random, string
from PIL import Image
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _
from datetime import date
from django.core.validators import (BaseValidator)


def get_filename(path): #/abc/filename.mp4
    return os.path.basename(path)


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_key_generator(instance):
    size = random.randint(30, 45)
    key = random_string_generator(size=size)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(key=key).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return key


def unique_verification_key_generator(instance):
    size = random.randint(10, 15)
    verification_key = random_string_generator(size=size)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(verification_key=verification_key).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return verification_key


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


@deconstructible
class MinAgeValidator(BaseValidator):
    compare = lambda self, a, b: calculate_age(a) < b
    message = _("Age must be at least %(limit_value)d.")
    code = 'min_age'


GENDER_CHOICES = (("Male", "Male"), ("Female", "Female"),("Other", "Other"))

STATUS_CHOICES = (("New", "New"), ("Completed", "Completed"), ("Process", "Process"), ("Need Help", "Need Help"),
                  ("Other", "Other"))