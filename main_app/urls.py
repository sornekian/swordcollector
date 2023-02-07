from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('swords/', views.swords_index, name='index'),
    path('swords/<int:sword_id>/', views.swords_detail, name='detail'),
    path('swords/create/', views.SwordCreate.as_view(), name='swords_create'),
    path('swords/<int:pk>/update/', views.SwordUpdate.as_view(), name='swords_update'),
    path('swords/<int:pk>/delete/', views.SwordDelete.as_view(), name='swords_delete'),
]
