from django.db import models

# Create your models here.
class Event(models.Model):

    event_image =  models.ImageField(upload_to= 'event_image/') # сохранение медиа файлов, как мы помним, в папке event_image
    event_text = models.CharField(max_length = 200)
    
