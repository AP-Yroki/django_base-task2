from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .forms import NewsForm, CategoryForm, AuthorForm, PublisherForm
from django.http import HttpResponseNotFound

def news_list(request):
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})

def edit_news(request, id):
    news = get_object_or_404(News, id=id)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm(instance=news)
    return render(request, 'edit.html', {'form': form})

def delete_news(request, id):
    news = get_object_or_404(News, id=id)
    news.delete()
    return redirect('news_list')

def index(request):
    news = News.objects.all()
    return render(request, 'index.html', context={'news': news})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PublisherForm()
    return render(request, 'add_publisher.html', {'form': form})