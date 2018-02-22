# _*_ coding=utf-8 _*_
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Type(models.Model):
    """通知的分类类别"""
    type = models.CharField(max_length=200)
    update_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """返回type的值"""
        return self.type


class Notice(models.Model):
    """通知的内容"""
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    text = models.TextField()
    update_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'notices'

    def __str__(self):
        """返回文本内容"""
        return self.text[:30]+'...'

