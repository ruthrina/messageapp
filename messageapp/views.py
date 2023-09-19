from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import messagedb

class homePageView(ListView):
    model = messagedb
    template_name = 'home.html'

    context_object_name = 'all_posts_list'
