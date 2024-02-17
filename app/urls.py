from django.urls import path, re_path

from . import views
from .views import page_not_found, BlogDetailView, CampaignDetailView, process_transaction

urlpatterns = [
    path('', views.index, name='index'),
    path('campaign/', views.page_donate, name='page_donate'),
    path('campaigns/<slug:slug>/', CampaignDetailView.as_view(), name='campaign_details'),
    path('process_zelle_transaction/', process_transaction, name='process_zelle_transaction'),
    path('contact/', views.page_contact, name='page_contact'),
    path('about/', views.page_about, name='page_about'),
    path('gallery/', views.page_gallery, name='page_gallery'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),

    # Ruta para manejar vistas no encontradas(404)
    re_path(r'^.*/$', page_not_found, name='page_not_found'),
]
