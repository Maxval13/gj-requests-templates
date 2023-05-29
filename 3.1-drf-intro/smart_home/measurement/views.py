from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


class SensorCreateAPIView(CreateAPIView, ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementListCreateAPIView(CreateAPIView, ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
