from django.utils.http import is_safe_url
from PIL import Image


class RequestFormAttachMixin(object):
    def get_form_kwargs(self):
        kwargs = super(RequestFormAttachMixin, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class NextUrlMixin(object):
    default_next = "app:index"

    def get_next_url(self):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        if is_safe_url(redirect_path, request.get_host()):
            return redirect_path
        return self.default_next


def handle_uploaded_file(profile_picture):
    img = Image.open(profile_picture.path)
    if img.height > 600 or img.width > 600:
        img.thumbnail((600, 600))
        return img.save(profile_picture.path)
