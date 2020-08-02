from django.shortcuts import render
from django.http import HttpResponse

categories = [
      {
            'category': 'Sports',
            'selected': True
      },

      {
            'category': 'Entertainment',
            'selected': True
      },
]
# Create your views here.
def index(request):
      return render(request, 'feed/feed.html')
