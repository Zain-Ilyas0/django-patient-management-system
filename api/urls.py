from django.urls import path
from . import views


urlpatterns = [
    path('patentdata/', views.PatientDataListCreate.as_view(), name="patient-view-create"),
    path('sidebar/', views.sidebar, name="sidebar"),
    # path('patentdata/<int:pk>/', views.PatientDataRetrieveUpdateDestroy.as_view(), name="update"),
    path("edit/<int:id>/", views.edit, name="edit"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path('header/', views.header),
    path('doctordata/', views.doctordata)
    
]