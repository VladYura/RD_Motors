from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import PartCard, Category, Cars
from django.contrib import messages


class CategoryAndCars:
    """Сортировка по категории и машине"""
    def get_category(self):
        category_name_list = PartCard.objects.values('category__name')
        queryset = Category.objects.filter(name__in=category_name_list)
        return queryset

    def get_cars(self):
        car_name_list = PartCard.objects.values('car__name')
        car_model_list = PartCard.objects.values('car__model')
        queryset = Cars.objects.filter(
            Q(name__in=car_name_list),
            Q(model__in=car_model_list)
        )
        return queryset


class PartsListView(ListView, CategoryAndCars):
    """Список товаров"""
    model = PartCard
    context_object_name = 'parts'
    queryset = PartCard.objects.all().order_by('-published_date')
    template_name = 'part_list.html'
    paginate_by = 21


class PartDetailView(DetailView):
    """Описание товара"""
    model = PartCard
    context_object_name = 'part'
    template_name = 'part_detail.html'
    slug_field = 'id'


class SearchList(ListView, CategoryAndCars):
    """Сортировка товаров"""
    template_name = 'part_list.html'
    paginate_by = 21
    context_object_name = 'parts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_data'] = self.request.GET
        return context

    def get_queryset(self):
        query_set = PartCard.objects.all()
        req = self.request.GET

        if req['category']:
            query_set = query_set.filter(category=req['category'])
        if req['car']:
            query_set = query_set.filter(car__url=req['car'])
        if req['article']:
            query_set = query_set.filter(article=req['article'])
        if req['year']:
            query_set = query_set.filter(car_year=req['year'])
        if 'filter' in req.keys():
            if req['filter'] == 'cheap':
                query_set = query_set.order_by('price')
            if req['filter'] == 'expensive':
                query_set = query_set.order_by('-price')

        if not query_set:
            messages.error(self.request, 'Таких товаров нет:( ')

        return query_set

