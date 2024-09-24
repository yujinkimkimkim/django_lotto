from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):

    class Meta:
        model = GuessNumbers
        fields = ('name', 'text', ) #name, text에 대한 입력만 받겠다는 뜻, 모델에 있는 필드명이랑 통일시킬 것
