from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

class ubicacionesViewSet(viewsets.ModelViewSet):
    model = ubicaciones
    queryset = ubicaciones.objects.all()
    serializer_class = ubicacionSerializer

