from django import forms


from .models import UploadFile, FileRec


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['file_path']
        labels = {'file_path': ''}


class FileRecForm(forms.ModelForm):
    class Meta:
        model = FileRec
        fields = ['file']
        labels = {'file': ''}
