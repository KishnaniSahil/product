from django.urls import path,include
from . import views

urlpatterns = [
      path('home/',views.home),
      path('about/',views.about)
    # localhost:8000/blog/home
]