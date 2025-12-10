from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofrectangle/', views.rectanglearea, name="areaofrectangle"),
    path('', views.rectanglearea, name="areaofrectangleroot"),
]