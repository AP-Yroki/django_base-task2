from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .forms import NewsForm
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
