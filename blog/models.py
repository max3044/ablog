from django.db import models

# Create your models here.

class Post(models.Model):

    post_image =  models.ImageField(upload_to= 'post_image/') # сохранение медиа файлов, как мы помним, в папке event_image
    post_title = models.CharField(max_length = 200, verbose_name = 'Заголовок')
    post_date = models.DateTimeField(auto_now=True)
    post_text= models.TextField(verbose_name ='Текст')

    
    def __str__(self):

        return self.post_title

    class Meta:

        verbose_name = "Пост"

        verbose_name_plural = "Посты"
