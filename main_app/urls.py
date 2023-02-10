from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('swordsmiths/', views.swordsmiths_index, name='index'),
    path('swordsmiths/<int:swordsmith_id>/', views.swordsmiths_detail, name='detail'),
    path('swordsmiths/create/', views.SwordsmithCreate.as_view(), name='swordsmiths_create'),
    path('swordsmiths/<int:pk>/update/', views.SwordsmithUpdate.as_view(), name='swordsmiths_update'),
    path('swordsmiths/<int:pk>/delete/', views.SwordsmithDelete.as_view(), name='swordsmiths_delete'),
    path('swordsmiths/<int:swordsmith_id>/add_sword/', views.add_sword, name='add_sword'),
    path('swordsmiths/<int:swordsmith_id>/assoc_warrior/<int:warrior_id>/', views.assoc_warrior, name='assoc_warrior'),
    path('swordsmiths/<int:swordsmith_id>/disassoc_warrior/<int:warrior_id>/', views.disassoc_warrior, name='disassoc_warrior'),
    path('warriors/', views.WarriorList.as_view(), name='warriors_index'),
    path('warriors/<int:pk>/', views.WarriorDetail.as_view(), name='warriors_detail'),
    path('warriors/create/', views.WarriorCreate.as_view(), name='warriors_create'),
    path('warriors/<int:pk>/update/', views.WarriorUpdate.as_view(), name='warriors_update'),
    path('warriors/<int:pk>/delete/', views.WarriorDelete.as_view(), name='warriors_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
