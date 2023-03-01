from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PartCard
from .forms import MainForm
from django.contrib import messages


class CategoryAndCars:

    def get_category(self):
        return PartCard.objects.order_by('category__name')

    def get_cars(self):
        return PartCard.objects.order_by('car__name')


class PartsListView(ListView, CategoryAndCars):
    """Список товаров"""
    model = PartCard
    queryset = PartCard.objects.all().order_by('-published_date')
    template_name = 'part_list.html'
    paginate_by = 20


class PartDetailView(DetailView):
    """Товар"""
    model = PartCard
    template_name = 'part_detail.html'
    slug_field = 'id'


class SearchList(ListView, CategoryAndCars):
    """Сортировка товаров"""
    template_name = 'part_list.html'

    def get_queryset(self):
        query_set = PartCard.objects.all()
        req = self.request.GET

        if req['category']:
            query_set = query_set.filter(category=req['category'])
        if req['car']:
            query_set = query_set.filter(car__name=req['car'])
        if req['article']:
            query_set = query_set.filter(article=req['article'])
        if req['year']:
            query_set = query_set.filter(car_year=req['year'])

        if not query_set:
            messages.error(self.request, 'Таких товаров нет:(')
            return

        return query_set

