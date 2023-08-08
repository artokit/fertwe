from django.urls import path
from .views import Index, CarsView

urlpatterns = [
    path('', Index.as_view()),
    path('cars/<int:pk>/', CarsView.as_view()),
]
