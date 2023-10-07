from typing import Any
from django.db import models
import os

# Create your models here.

class FileExchange(models.Model):
    id = models.AutoField(primary_key=True)
    file_path = models.FileField(upload_to='files/%Y/%m/%d/', blank=False, null=False)
    code = models.CharField(max_length=10, null=False, blank=False)
    creation_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "file_exchange"

    def delete(self):
        if self.file_path:
            if os.path.isfile(self.file_path.path):
                os.remove(self.file_path.path)

        return super().delete()

    def __str__(self) -> str:
        return str(self.id)