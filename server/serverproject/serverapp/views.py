import json

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class ServerApiView(APIView):

    def get(self, request, format=None):
        if not request.data:
            return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
        try:
            json_data = json.loads(request.data)
        except TypeError:
            return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
        x = json_data.get('value1')
        y = json_data.get('value2')
        if x is None or y is None:
            return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
        result_object = {"result": x+y}
        return Response(result_object)


class LiveApiView(APIView):

    def get(self, request, format=None):
        return Response('I am alive', status=status.HTTP_200_OK)
