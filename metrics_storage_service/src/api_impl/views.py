from django.http import HttpResponse
from django.views.generic.base import View

from .utils import log


class TempView(View):
    @staticmethod
    @log()
    def dispatch(_, *args, **kwargs):
        return HttpResponse('Just first step')
