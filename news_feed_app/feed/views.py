from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from .models import *
from .forms import *

from newsapi import NewsApiClient

NEWS_API_KEY = 'd7ec041620bb4809bee18d2a5e9fab09'
api = NewsApiClient(api_key=NEWS_API_KEY)

article_categories = {'sports':[], 'general':[], 'business':[], 'entertainment':[], 'health':[], 'science':[], 'technology':[]}

def update_news_feed():
    categories =  Category.objects.all()
    for category in categories:
        if category.selected == True:
            response = api.get_top_headlines(country='us',category=category.name)
            article_categories[category.name] = response['articles'][0:5]
        else:
            article_categories[category.name] = []

def initialize_category_form(form):
    categories = Category.objects
    for category in form.fields:
        form.fields[category].initial =  categories.filter(name=category).get().selected

def update_database(form):
    categories = form.clean()
    categoriesObj =  Category.objects.all()
    for category in categories:
        obj = categoriesObj.filter(name=category).update(selected=categories[category])

# Home page view 
def home(request):
    form = CategoryForm()
    initialize_category_form(form)

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            update_database(form)
            return redirect('/')
    else:
        update_news_feed()

    context = { 'form':form, 'article_categories':article_categories }
    return render(request, 'feed/home.html', context)

def search_news(request):
    search_results = []
    if request.method == 'GET':
        search_query = request.GET.get('q') 
        response = api.get_everything(q=search_query)
        search_results = response['articles']
    else:
        return redirect('/')

    context = { 'search_results': search_results }
    return render(request, 'feed/news_search_results.html', context)