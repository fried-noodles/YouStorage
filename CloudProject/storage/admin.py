from django.contrib import admin
from .models import UploadFile, FileRec

# Register your models here.
admin.site.register(UploadFile)
admin.site.register(FileRec)
