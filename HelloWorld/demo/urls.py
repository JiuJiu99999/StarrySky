from django.urls import path
from . import views

urlpatterns = [
    path('', views.toLogic_view),
    path('index/', views.login_view),
    path('toregister/', views.toregister_view),
    path('register/', views.register_view),
]