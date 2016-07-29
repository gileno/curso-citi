# coding=utf-8

import random

from django.http import HttpResponse


class LogMiddleware(object):

    def process_request(self, request):
        if random.randint(1, 5) == 2 and request.path == '/':
            return HttpResponse('Perdeu')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(view_func)

    def process_response(self, request, response):
        print('response')
        return response
