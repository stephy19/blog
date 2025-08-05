from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comments , Category
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from blogapp.forms import CommentsForm
from blogapp.forms import SearchPost, PostForm
from django.contrib.postgres.search import SearchVector
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import get_user_model
import json
import time
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import HttpResponse, StreamingHttpResponse
# Create your views here.
def post_list(request, category=None,*args, **kwargs):
    now = timezone.now()
    posts = Post.published.all()
    categories = Category.objects.all()
    if category:
        category = get_object_or_404(Category, slug=category)
        posts = posts.filter(category=category)
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'page': page,
        'categories': categories,
        'category': category,
        'now': now
    }
    return render(request, 'blog/post/liste.html',context)

def post_detail(request, slug : str):  
    
    User = get_user_model()
    superuser = User.objects.filter(is_superuser=True).first()
    suser = superuser.username
    categories = Category.objects.all()
    post = get_object_or_404(Post, slug=slug)
    comments = Comments.objects.filter(post=post.id)
    page = request.GET.get('page')
    paginator = Paginator(comments, 2)
    
    try:
        comment = paginator.page(page)
    except PageNotAnInteger:
        comment = paginator.page(1)
    except EmptyPage:
        comment = paginator.page(paginator.num_pages)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentsForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comment_form = CommentsForm()
        
    context = {
        'post': post,
        'comments': comment,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'categories': categories,
        'superuser': suser
    }
        
    return render(request, 'blog/post/detail.html',context)


def post_search(request):
    query = None
    results = []
    search_form = SearchPost()
    if 'query' in request.GET:
        search_form = SearchPost(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            results = Post.published.annotate(search=SearchVector("title", "body")).filter(search=query)
           
    return render(request, 'blog/post/search.html', {
                'results': results,
                'query': query,
                'search_form': search_form
            })

def add_post(request):
    messages= ""
    if request.user.is_authenticated:
        if request.method=='POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.author = request.user
                obj.save()
                messages = "Post créé avec succès , l'administrateur validera votre post dans les plus brefs délais"
                return render(request, 'blog/post/add.html', {'form': form , 'message': messages})
        else:
            form = PostForm()
            return render(request, 'blog/post/add.html', {'form': form })
    else:
        return redirect('accounts:login')
    
def post_update(request, slug : str, *args, **kwargs):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_authenticated:
        if post.author == request.user:
                if request.method=='POST':
                    form = PostForm(request.POST, request.FILES, instance=post)
                    if form.is_valid():
                        obj = form.save(commit=False)
                        obj.author = request.user
                        obj.save()
                        return redirect('blogapp:post_detail', slug=post.slug)
                else:
                    form = PostForm(instance=post)
                return render(request, 'blog/post/update.html', {'form': form})
        else:
            return redirect('blogapp:post_detail')
    else:
        return redirect('accounts:login')



def stream_view(request,post_id):
    def event_stream():
        initial_data = ''
        commments = commments.objects.filter(post_id=post_id)\
             .values('body', 'created', 'author__username', 'post__id')
        while True:
            data = json.dumps(list(commments.values()), cls=DjangoJSONEncoder)
            if not initial_data == data:
               yield '\n'
               yield f'data: {data}'
               yield '\n\n'
            time.sleep(1)
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')





def post_delete(request, slug : str, *args, **kwargs):
    messages= 'Votre post à été supprimé avec succès !'
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_authenticated:
        if post.author == request.user:
            post.delete()
        return render(request, 'blog/post/delete.html', {'message': messages})
    else:
        return redirect('accounts:login')