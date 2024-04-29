from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from Authapp.permissions import check_is_creator_or_admin
from app.lastviewed import last_viewed_info
def home(request):
   posts = Post.objects.all()


   return render(request, 'home.html', {'posts':posts})

@login_required
def new(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        new_post = Post.objects.create(
            title=title, content=content, creator=request.user
        )
        return redirect("detail", new_post.pk)

    return render(request, "new.html")   

@login_required
@last_viewed_info(Post)
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            post=post,
            content=content
        )
        return redirect('detail', post_pk)

    return render(request, 'detail.html', {'post': post})





@login_required
@check_is_creator_or_admin(Post, "post_pk")
def edit(request, post_pk):
   post = Post.objects.get(pk=post_pk)


   if request.method == 'POST':
       title = request.POST['title']
       content = request.POST['content']
       Post.objects.filter(pk=post_pk).update(
           title=title,
           content=content
       )
       return redirect('detail', post_pk)


   return render(request, 'edit.html', {'post':post})



@login_required
@check_is_creator_or_admin(Post, "post_pk")
def delete(request, post_pk):
   post = Post.objects.get(pk=post_pk)
   post.delete()


   return redirect('home')

@login_required
@check_is_creator_or_admin(Comment, "comment_pk")
def delete_comment(request, post_pk, comment_pk):
   comment = Comment.objects.get(pk=comment_pk)
   comment.delete()
   return redirect('detail',post_pk)

def base(requset):
    return render(requset, 'base.html')


    
