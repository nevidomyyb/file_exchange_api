from django.shortcuts import render
from .models import FileExchange
from .serializers import FileManagerSerializer
from rest_framework.generics import CreateAPIView
# Create your views here.

class FilePostView(CreateAPIView):
    queryset = FileExchange.objects.all()
    serializer_class = FileManagerSerializer
