from django import forms
from django.db import models

from .models import Tweet

class TweetFrom(forms.ModelForm):
  class Meta:
    model = Tweet
    fields = ('tweeted_at', 'text', 'img')