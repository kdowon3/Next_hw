from functools import wraps
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def last_viewed_info(model_cls):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            post_pk = kwargs.get('post_pk')
            if post_pk is None:
                return render(request, "error.html", {"error": "Post ID not found."})

            post = get_object_or_404(model_cls, pk=post_pk)

            if request.user.is_authenticated:
                post.last_viewed_time = timezone.now()
                post.last_viewed_user = request.user
                post.save()

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
