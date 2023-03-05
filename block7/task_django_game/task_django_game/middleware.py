import logging

logger = logging.getLogger(__name__)


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(f'Incoming request: {request.method} {request.path}')

    def process_template_response(self, request, response):
        print(f'Outgoing response: {response.status_code}')
        return response
