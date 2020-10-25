from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('courses/<slug>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('courses/<slug>/<video_slug>/', views.VideoDetailView.as_view(), name='video-detail'),
    path('payment/enroll/', views.EnrollView.as_view(), name='enroll'),
    path('payment/enroll/<slug>/', views.PaymentView, name='payment'),
    path('payment/create-subscription/', views.CreateSubscriptionView.as_view(), name='create-subscription'),
    path('payment/change-subscription/', views.ChangeSubscriptionView.as_view(), name='change-subscription'),
    path('payment/retry-invoice/', views.RetryInvoiceView.as_view(), name='retry-invoice'),
    path('payment/webhook/', views.webhook, name='webhook'),
]
