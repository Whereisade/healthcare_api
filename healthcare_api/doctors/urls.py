from django.urls import path
from .views import DoctorProfileCreateUpdateView, DoctorProfileListView

urlpatterns = [
    path('doctors/', DoctorProfileListView.as_view(), name='doctor-list'),
    path('doctors/manage/', DoctorProfileCreateUpdateView.as_view(), name='doctor-create-update'),
]
