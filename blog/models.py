from django.db import models
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='blog_posts')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Новий пост'
        verbose_name_plural = 'Нові пости'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    # user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=80, verbose_name='Ім`я')
    email = models.EmailField(max_length=254, verbose_name='Email')
    title = models.TextField(max_length=200, verbose_name='Заголовок')
    comment = models.TextField(max_length=5000, verbose_name='Коментар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    

    class Meta:
        db_table = 'blog_comment'
        ordering = ['created_at']
        verbose_name = 'Новий коментар'
        verbose_name_plural = 'Нові коментарі'

    def __str__(self):
        return 'Comment {} by {}'.format(self.title, self.name)
