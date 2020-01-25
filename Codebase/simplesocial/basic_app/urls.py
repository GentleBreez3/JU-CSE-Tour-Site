from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.MoneyListView.as_view(),name='list'),
    path('<int:pk>/',views.MoneyDetailView.as_view(),name='detail'),
    path('create/',views.MoneyCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.MoneyUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.MoneyDeleteView.as_view(),name='delete')
]
