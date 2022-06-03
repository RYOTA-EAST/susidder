from django.views.generic import ListView, FormView, CreateView, UpdateView, View

from .models import Tweet

class IndexView(ListView):

  template_name = 'twitter/index.html'
  context_object_name = 'tweets'
  queryset = Tweet.objects.filter(is_sent=False, is_deleted=False)

index = IndexView.as_view()