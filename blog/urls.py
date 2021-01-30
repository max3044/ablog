from django.urls import path

from . import views


urlpatterns = [
    
    path('', views.showblog, name = 'blog'),

    # <int:post_id>/ - значит, что дажнго будет сохранять целое число, которое оно будет получать из url в переменной post_id

    path('<int:post_id>/', views.current_post, name='current_post')



] 