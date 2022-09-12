from django.urls import path
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import Static_Sitemap
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us/', views.contact, name='contact_us'),
    path('booking/', views.booking, name='booking'),
    path('book-with-us/', views.booking_page, name='booking_page'),
    path('inner-page/', views.inner_page, name='inner_page'),
    path('sitemap.xml', sitemap, {'sitemaps': {"static": Static_Sitemap}},
         name='django.contrib.sitemaps.views.sitemap')
    # path('privacy-policy/', views.privacy, name='privacy'),
    # path('disclaimer/', views.disclaimer, name='disclaimer'),
]