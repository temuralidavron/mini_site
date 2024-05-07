from django.shortcuts import render,redirect
from .forms import BlogForm
from .models import Blog, News, Like


def news_list(request):
    news = News.objects.all()
    user = request.user
    context = {
        'news': news,
        'user': user,
    }
    return render(request, 'new/news_list.html', context)

def news_post(request, pk):


    news_object = News.objects.get(id=pk)
    news_object.news_views = news_object.news_views + 1
    news_object.save()


    context = {
        'new': news_object,
    }
    return render(request, 'new/news_detail.html', context)



def like_post(request):
    user = request.user
    if request.method == 'POST':
        new_id = request.POST.get('new_id')
        new = News.objects.get(id=new_id)
        if user in new.liked.all():
            new.liked.remove(user)
        else:
            new.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, news_id=new_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()

    return redirect('news_list')



def blog_list(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog_list.html',context )

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()


    return render(request, 'blog/create_blog.html',{'form':form})


def blog_update(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog/create_blog.html', {'form':form})

def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog_detail.html', context)