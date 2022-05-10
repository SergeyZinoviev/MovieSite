from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import F
from django.views.generic.base import View
from .forms import ReviewForm

class Home(ListView):
    model = Post
    template_name = 'movie/index.html'
    context_object_name = 'posts'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Фильм'
        return context


class PostsByCategory(ListView):
    template_name = 'movie/category.html'
    context_object_name = 'posts'    
    paginate_by = 50
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context    


class GetPost(DetailView):
    model = Post
    template_name = 'movie/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context 


class Search(ListView):
    template_name = 'movie/search.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['s'] = f"s={self.request.GET.get('s')}"
        return context


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Post.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


def news(request):
    return render(request, 'movie/news.html')


def comsoon(request):
    return render(request, 'movie/comsoon.html')

# def get_post(request, slug):
#     return render(request, 'movie/index.html')

