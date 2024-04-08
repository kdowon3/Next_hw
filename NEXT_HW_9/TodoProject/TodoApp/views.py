from django.shortcuts import render, redirect
from .models import Post
from datetime import datetime  # 추가

# Create your views here.
def home(request):
    posts = Post.objects.order_by('deadline')
    return render(request, 'home.html', {'posts': posts})

def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            deadline=request.POST['deadline'],
        )
        return redirect('detail', new_post.pk)
        
    return render(request, 'new.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    return render(request, 'detail.html', {'post': post})

def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        deadline_str = request.POST['deadline']
        if deadline_str:  # 폼에서 날짜 및 시간 값이 비어있지 않은 경우에만 처리
            post.deadline = datetime.strptime(deadline_str, '%Y-%m-%dT%H:%M')  # 입력된 값을 올바른 형식으로 변환
        post.save()  
        return redirect('detail', post_pk=post_pk)
    return render(request, 'update.html', {'post': post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')
