from django.urls import path
from api_final.views import contenido_api_view

urlpatterns = [
    path('crear-contenido/', contenido_api_view.as_view()),
    path('actualizar-contenido/<int:pk>/', contenido_api_view.as_view(), name='actualizar'),
    path('eliminar-contenido/<int:pk>/', contenido_api_view.as_view(), name='eliminar'),
]
