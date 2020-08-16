from django.shortcuts import render
from .models import Article

# Create your views here.


def blog(request):
    articles = Article.objects.all()
    data = {'articles': articles}
    return render(request, 'blog/blog.html', data)


def detail(request, article_id):
    article_data = Article.objects.get(pk=article_id)
    data = {'article_data': article_data}
    return render(request, 'blog/article.html', data)
