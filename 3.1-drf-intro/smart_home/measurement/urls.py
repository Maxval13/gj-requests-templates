from django.urls import path

from .views import SensorCreateAPIView, SensorRetrieveUpdateAPIView, MeasurementListCreateAPIView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorCreateAPIView.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveUpdateAPIView.as_view()),
    path('measurements/', MeasurementListCreateAPIView.as_view()),
]
