from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {'blog': blog}
    return render(request, 'blog/blog_detail.html', context)

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    context = {'form': form}
    return render(request, 'blog/blog_form.html', context)

def blog_update(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    context = {'form': form}
    return render(request, 'blog/blog_form.html', context)

def blog_delete(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    context = {'blog': blog}
    return render(request, 'blog/blog_delete.html', context)
