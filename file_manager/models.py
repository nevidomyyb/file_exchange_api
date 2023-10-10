from collections.abc import Iterable
from typing import Any
from django.db import models
from string import ascii_letters, digits
import random
import os

# Create your models here.

class FileExchange(models.Model):
    id = models.AutoField(primary_key=True)
    file_path = models.FileField(upload_to='files/%Y/%m/%d/', blank=False, null=False)
    code = models.CharField(max_length=10, null=False, blank=False)
    downloaded = models.BooleanField(default=0)
    creation_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "file_exchange"

    def save(self, *args, **kwargs):
        valid_digits = [*ascii_letters, *digits]
        code_len = random.randint(0, 9)
        code = ""
        for i in range(0, code_len):
            rand_value = random.randint(0,len(valid_digits))
            code+=valid_digits[rand_value-1]
        self.code = code
        return super(FileExchange, self).save(*args, **kwargs)

    def delete(self):
        if self.file_path:
            if os.path.isfile(self.file_path.path):
                os.remove(self.file_path.path)

        return super().delete()

    def __str__(self) -> str:
        return str(self.id)