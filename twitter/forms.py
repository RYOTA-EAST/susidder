from django import forms
from django.db import models

from .models import Tweet

class TweetForm(forms.ModelForm):
  img = forms.ImageField(
    label='ツイート画像',
    required=False,
    error_messages={'invalid': '画像のみ可能です'},
    widget=forms.FileInput()
  )

  class Meta:
    model = Tweet
    fields = ('tweeted_at', 'text', 'img')