from django.shortcuts import render, get_list_or_404, redirect
from .models import Post
from .form import PostForm
from django.utils import timezone

# Create your views here.
def post_list(request):
    context = Post.objects.all()
    return render(request, 'home/post_list.html', {"posts": context})

def post_details(request, pk):
    posts = get_list_or_404(Post.objects.all(), pk=pk)
    return render(request, 'home/post_details.html', {"posts": posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'home/post_edit.html', {"form": form})