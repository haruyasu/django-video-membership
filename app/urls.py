from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('courses/<slug>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('courses/<slug>/<video_slug>/', views.VideoDetailView.as_view(), name='video-detail'),
]
