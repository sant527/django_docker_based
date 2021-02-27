from project import settings

def RequestExposerMiddleware(get_response):
    def middleware(request):
        settings.exposed_request = request
        response = get_response(request)
        return response

    return middleware