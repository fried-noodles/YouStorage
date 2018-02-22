# -*- coding: UTF-8 -*-
from django import forms

from .models import Type, Notice


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ('type',)
        labels = {'type': ''}


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
