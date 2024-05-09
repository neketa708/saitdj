from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='index'),
    path('about/', views.about, name='about'),
    path('if/', views.my_view, name='if'),
    path('ab/', views.TemplIf.as_view(), name='ab'),
    path('zz/', views.user_form, name='zz'),
]