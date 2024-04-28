from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    #path('contact-us/', views.contact_us, name='contact_us'),
    #path('contact-us/success/', views.contact_us_success, name='contact_us_success'),  # Success page view
]