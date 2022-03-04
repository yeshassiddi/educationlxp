from django.utils.deprecation import MiddlewareMixin
from django.utils import translation

class AdminLocaleMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path.startswith('/admin'):
            translation.activate("en")
            request.LANGUAGE_CODE = translation.get_language()
