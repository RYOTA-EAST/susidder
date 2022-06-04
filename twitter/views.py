from django.views.generic import ListView, FormView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Tweet
from .forms import TweetForm

class IndexView(ListView):

  template_name = 'twitter/index.html'
  context_object_name = 'tweets'
  queryset = Tweet.objects.filter(is_sent=False, is_deleted=False)

index = IndexView.as_view()

class FormViewBase(FormView):
  model = Tweet
  template_name = 'twitter/form.html'
  success_url = reverse_lazy('twitter:index')
  form_class = TweetForm
  message = ''

  def form_valid(self, form):
    tweet = form.save(commit=False)
    tweet.user_id = self.request.user.id
    tweet.save()
    messages.success(self.request, '成功しました')

class TweetCreateView(FormViewBase):
  message = 'ツイートを予約しました'

create = TweetCreateView.as_view()

class TweetUpdateView(FormViewBase, UpdateView):
  message = '予約ツイート内容を変更しました'

update = TweetUpdateView.as_view()