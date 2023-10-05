from django.contrib import admin
from .models import FileExchange

# Register your models here.

class FileExchangeAdmin(admin.ModelAdmin):
    ...

admin.site.register(FileExchange, FileExchangeAdmin)
