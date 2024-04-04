from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm  # ArticleForm 추가

def new(request):
    if request.method == 'POST':
        new_article = Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category']  # 새로운 카테고리 값 추가
        )
        return redirect('list')
    
    return render(request, 'new.html')


def list(request):
    categories = Article.CATEGORY_CHOICES
    category_counts = {category[0]: Article.objects.filter(category=category[0]).count() for category in categories}
    articles = Article.objects.all()
    return render(request, 'list.html', {'articles': articles, 'category_counts': category_counts})

def detail(request, article_id):
    article = Article.objects.get(id = article_id)
    return render(request, 'detail.html', {'article': article})

def category_board(request, category):
    articles = Article.objects.filter(category=category)
    return render(request, f'category_board_{category}.html', {'articles': articles, 'category': category})

def get_category_counts():
    categories = ['취미', '음식', '프로그래밍']
    category_counts = {}
    for category in categories:
        count = Article.objects.filter(category=category).count()
        category_counts[category] = count
    return category_counts