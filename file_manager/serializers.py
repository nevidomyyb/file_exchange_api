from rest_framework import serializers
from .models import FileExchange
import os
import random
from django.core.exceptions import ValidationError
from rest_framework.serializers import RelatedField
from string import ascii_letters, digits

class CreateCodeField(RelatedField):

    def to_representation(self, value):
        if value: raise ValidationError('Please do not send a code value')
        valid_digits = [*ascii_letters, *digits]
        code_len = random.randint(0, 9)
        code = ""
        for i in range(0, code_len):
            rand_value = random.randint(0,len(valid_digits))
            code+=valid_digits[rand_value]
        value = code
        return code

def validate_file_extensions(value):
    extension = os.path.splitext(value.name)[1].lower()
    valid_extensions =  ['.pdf', '.xls', '.xlsx', '.rar', '.jpg', '.jpeg', '.png', '.gif', '.txt']
    if not extension in valid_extensions:
        raise ValidationError('Unsupported file extension')

class FileManagerSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False, read_only=True)
    file_path = serializers.FileField()
    creation_at = serializers.DateTimeField(required=False, read_only=True)

    class Meta:
        model = FileExchange
        fields = ['id', 'file_path', 'creation_at']
    
    def validate_file_path(self, value):
        validate_file_extensions(value)
        return value
