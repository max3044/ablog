from django.shortcuts import render, get_object_or_404  # get_object_or_404 - получает либо объект по айди, либо возращает 404 страницу

from .models import Post

# Create your views here.


def showblog(request):
    
    
    posts = Post.objects

    return render(request, 'blog/blog.html', 
    {
        'posts' : posts
    }
    )

    
# как мы помним, мы указали, что число, полученной из url будет сохраняться в переменной, эту переменную мы передаём в функцию
def current_post(request, post_id):

    post = get_object_or_404(Post, pk=post_id) # get_object_or_404 принимает модель и идентификтор (т.е. она ищет объект в моделе под этим идентификатором)


    return render(request, 'blog/current_post.html', 
    {'post': post})

    