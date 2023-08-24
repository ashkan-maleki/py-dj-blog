from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post

import logging

logger = logging.getLogger(__name__)


def post_list(request):
    posts = Post.published.all()
    logger.debug(type({'posts': posts}))
    return render(request, template_name='blog/post/list.html', context={'posts': posts})


def post_detail(request, id, year, month, day, post):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     return Http404("No post found")
    # post = get_object_or_404(Post,id=id, status=Post.Status.PUBLISHED)
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # return render(request, 'blog/post_list.html', {'posts': posts})
    logger.debug(type({'post': post}))
    return render(request, template_name='blog/post/detail.html', context={'post': post})
