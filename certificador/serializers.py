from rest_framework import serializers
from .models import ubicaciones

class ubicacionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ubicaciones
		fields = '__all__'

