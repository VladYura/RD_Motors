from django.urls import path
from .views import PartsListView, PartDetailView


urlpatterns = [
    path('', PartsListView.as_view(), name='home'),
    path('<int:pk>/', PartDetailView.as_view(), name='part-card-detail'),
]
