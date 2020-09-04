"""Timestamp middleware"""
from datetime import datetime


class RequestTimeStampMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        response = self.get_response(request)
        return response
