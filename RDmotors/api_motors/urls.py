from django.urls import path

from . import views

urlpatterns = [
    path('parts/', views.PartCardListView.as_view()),
    path('parts/<int:pk>/', views.PartCardDetailView.as_view()),
    path('categories/', views.CategoryListView.as_view()),
    path('cars/', views.CarsListView.as_view()),
]
