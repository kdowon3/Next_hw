from django.shortcuts import render, redirect
from .models import Post, Comment, Reply


def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category']  # 새로운 카테고리 값 추가
        )
        return redirect('list')
    
    return render(request, 'new.html')


def list(request):
    categories = Post.CATEGORY_CHOICES
    category_counts = {category[0]: Post.objects.filter(category=category[0]).count() for category in categories}
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts': posts, 'category_counts': category_counts})

def detail(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    
    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            post = post,
            content = content
        )
        return redirect('detail', post_pk)
    return render(request, 'detail.html', {'post': post})

def category_board(request, category):
    posts = Post.objects.filter(category=category)
    return render(request, f'category_board_{category}.html', {'posts': posts, 'category': category})

def get_category_counts():
    categories = ['취미', '음식', '프로그래밍']
    category_counts = {}
    for category in categories:
        count = Post.objects.filter(category=category).count()
        category_counts[category] = count
    return category_counts

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail',post_pk)


def add_reply(request, post_pk, comment_pk):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        reply_content = request.POST.get('reply_content')  # 올바른 메소드명 사용
        Reply.objects.create(comment=comment, content=reply_content)  # 대댓글 생성
        return redirect('detail', post_pk=post_pk)  # 대댓글 생성 후 원래 페이지로 리다이렉트
    else:
        return redirect('detail', post_pk=post_pk)
    
def delete_reply(request, reply_pk):
    # 대댓글 객체를 가져오거나 404 에러를 발생시킵니다.
    reply = Reply.objects.get(pk=reply_pk)

    # 대댓글을 삭제합니다.
    reply.delete()

    # 대댓글이 삭제된 후 원래 페이지로 리다이렉트합니다.
    return redirect('detail', post_pk=reply.comment.post.pk)

def base(request):
    return render(request, 'base.html')