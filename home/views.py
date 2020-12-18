from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class IndexView(APIView):
    """API landing response"""
    permission_classes = [AllowAny, ]

    def get(self, request, format=None):
        return Response({'message': 'Welcome to the ResourceIdea API'})
