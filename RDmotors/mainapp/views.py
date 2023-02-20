from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PartCard


class PartsListView(ListView):
    """Список товаров"""
    model = PartCard
    template_name = 'index.html'
    paginate_by = 20


class PartDetailView(DetailView):
    """Товар"""
    model = PartCard
    template_name = 'part_detail.html'
