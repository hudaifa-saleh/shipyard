from django.urls import path, re_path

from shipyard.service import views

app_name = 'service'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path('category/<slug:slug>/', views.ServiceCategoryDetailView.as_view(), name='service-category-detail'),
]
