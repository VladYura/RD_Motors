from django.urls import path
from .views import PartsListView, PartDetailView, SearchList


urlpatterns = [
    path('', PartsListView.as_view(), name='home'),
    path('search/', SearchList.as_view(), name='search'),
    path('detail/<int:pk>/', PartDetailView.as_view(), name='part-card-detail'),
]
