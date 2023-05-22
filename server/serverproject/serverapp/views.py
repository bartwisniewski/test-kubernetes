import json

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class ServerApiView(APIView):

    def get(self, request, format=None):
        values = json.loads(request.data)
        x = values.get('value1')
        y = values.get('value2')
        if x is None or y is None:
            return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
        result_object = {"result": x+y}
        return Response(result_object)
