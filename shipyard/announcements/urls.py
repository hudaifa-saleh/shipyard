from django.urls import path

from . import views

app_name = 'announcements'
urlpatterns = [
    path('', views.AnnouncementListView.as_view(), name='list'),
    path('feed/', views.AnnouncementFeedView, name='feed'),

]
