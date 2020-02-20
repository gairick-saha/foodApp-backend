from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', csrf_exempt(views.simple_categories), name='ApiHome'),
    path('<str:slug>/', csrf_exempt(views.slug_categories), name='ApiHome'),
    path('<str:slug>/menu/', csrf_exempt(views.simple_menu), name='Menu'),
    path('<str:slug>/menu/<slug:menu_slug>/', csrf_exempt(views.slug_menu), name='Menu')
]
