from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UploadFile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    file_path = models.FileField(upload_to='./upload/%Y/%m/%d/')
    upload_time = models.DateTimeField(auto_now_add=True)
    share_opt = models.BooleanField(primary_key=0)

    def __str__(self):
        return self.name


class FileRec(models.Model):
    OPT_TYPE = (
        ('U', 'upload'),
        ('D', 'download'),
        ('R', 'delete'),
        ('S', 'share')
    )
    oprtr = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ForeignKey(UploadFile, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=1, choices=OPT_TYPE)

    def __str__(self):
        return self.file

