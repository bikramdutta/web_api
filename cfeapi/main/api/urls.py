
from django.urls import path
from .views import (
	UpdateModelDetailAPIView,
	UpdateModelListAPIView
	)



urlpatterns = [
    path('', UpdateModelListAPIView.as_view()), # List, Create,
    path(r'^(?P<id>\d+)/$', UpdateModelDetailAPIView.as_view()), # Retrieve, Update, Delete
]
 