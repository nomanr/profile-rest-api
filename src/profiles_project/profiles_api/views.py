from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .import serializers


# Create your views here.


class HelloApiView(APIView):
    """Test API Views."""

    serializers_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """Return a  list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'It is similar to tradational Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'hello!','an_apiview': an_apiview})


    def post (self, request):
        """Create a hello message with a name."""

        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message' : message̵})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handles updating object"""

        return Response({'method' : 'put' })

    
    def patch(self, request, pk=None):
        """Hanldes updating a prtial object"""

        return Response({'method' : 'patch' })
        
    
    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({'method' : 'delete' })



class HelloViewSet(viewsets.ViewSet):
    """Test API viewSet."""

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (lists, create, delete, update, partial_update',
            'Authomically maps to URLs using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'message' : 'Hello!', 'a_viewset' : a_viewset})