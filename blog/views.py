from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Post

def index(request):
    posts = Post.objects.all()

    return render(request, 'blog/index.html', {'posts': posts})

def detail(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('detail', pk=pk)
    else:
        form = CommentForm()

    form = CommentForm()

    return render(request, 'blog/detail.html', {'post': post, 'form': form})