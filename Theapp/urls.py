from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hithere', views.hithere),
    path('number/', views.evenodd),
    path('views/', views.index),
    path('tables/', views.table),
    path('table/', views.table2),
    path('variable/', views.variables),
    path('employee/', views.employee),
    path('', views.images),
    path('background/', views.background),

]