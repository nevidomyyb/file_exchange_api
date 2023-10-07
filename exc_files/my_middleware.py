from file_manager.models import FileExchange

class MyMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path[0:10] in '/api/file/':
            code_un = request.path[10:]
            index = code_un.index('/')
            code = code_un[:index]
            instance = FileExchange.objects.get(code=code)
            instance.delete()
            
        return response