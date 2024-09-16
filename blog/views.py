from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404


from blog.models import Blog, BlogComment


# Create your views here.
def blog(request):
    page = request.GET.get('page', 1)
    query = request.GET.get('q', None)
    
    if query:
        # Если есть поисковый запрос, фильтруем посты по полям заголовка или содержимого
        posts = Blog.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by('-created_at')
    else:
        # Если запроса нет, показываем все посты
        posts = Blog.objects.order_by('-created_at')
    
    paginator = Paginator(posts, 6)  
    current_page = paginator.page(int(page))

    context = {
        'posts': current_page,
        'query': query,
    }
    return render(request, 'blog/blog.html', context)

def blog_details(request, slug):
    
    post = get_object_or_404(Blog, slug=slug)
    comments = BlogComment.objects.filter(blog=post)
    comment_count = comments.count()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        comment_text = request.POST.get('comment')
        
        # Валидация полей
        if name and email and title and comment_text:
            BlogComment.objects.create(
                blog=post,
                name=name,
                email=email,
                title=title,
                comment=comment_text
            )
            return redirect('blog:blog_details', slug=slug)
        else:
            # Обработка ошибки, если данные не заполнены
            error_message = "Усі поля обов'язкові для заповнення."
            context = {
                'post': post,
                'comments': comments,
                'error_message': error_message
            }
            return render(request, 'blog/blog_details.html', context)

    context = {
        'post': post,  
        'comments': comments, 
        'comment_count': comment_count, 
    }
    return render(request, 'blog/blog_details.html', context)

    
