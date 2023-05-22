from rest_framework import serializers


class ClientSerializer(serializers.Serializer):
    value1 = serializers.IntegerField(default=2)
    value2 = serializers.IntegerField(default=2)
