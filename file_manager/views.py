from django.shortcuts import render
from .models import FileExchange
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from .serializers import FileManagerSerializer
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView
# Create your views here.

class FilePostView(CreateAPIView):
    queryset = FileExchange.objects.all()
    serializer_class = FileManagerSerializer

class FileDownloadView(GenericAPIView):

    queryset = FileExchange.objects.all()

    def get(self, request, code):
        try: instance = FileExchange.objects.get(code=code)
        except: return Response(status=HTTP_404_NOT_FOUND)
        self.instance = instance
        try:
            file_handle = instance.file_path.open()

            response = FileResponse(file_handle, content_type='arquivo')
            response['Content-Length'] = instance.file_path.size
            response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file_path.name
           
            return response

        except:
            return Response({"message": "Error while trying to send the archive"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
