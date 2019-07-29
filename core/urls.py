from django.urls import path

from . import views


urlpatterns = [
    path('search/', views.Search.as_view(), name='search'),
    path('addItem/',views.Add.as_view(),name='add'),
    path('<int:pk>/', views.ItemDetailView.as_view(), name='detail'),
    path('addImage/<int:pk>/', views.AddImageView.as_view(), name='image'),
    path('',views.Index.as_view(),name='index'),
]