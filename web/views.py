from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'web/post_list.html', {'posts': posts})
