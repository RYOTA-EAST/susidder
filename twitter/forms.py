from dataclasses import fields
from django.db import models
from .models import Tweet

class TweetFrom(forms.ModelForm):
  class Meta:
    model = Tweet
    fields = ('tweet_at', 'text', 'img')