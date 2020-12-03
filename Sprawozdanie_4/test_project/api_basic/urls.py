from django.urls import path
from .views import gallery_list, gallery_detail

urlpatterns = [
    path('gallery/', gallery_list),
    path('detail/<int:pk>/', gallery_detail)
]
