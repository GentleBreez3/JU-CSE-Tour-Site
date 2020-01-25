from django.urls import path
from . import views

app_name = 'tour'

urlpatterns = [
    path('',views.StudentsListView.as_view(),name='list'),
    path('<int:pk>/',views.StudentsDetailView.as_view(),name='detail'),
    path('create/',views.StudentsCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.StudentsUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.StudentsDeleteView.as_view(),name='delete')
]
