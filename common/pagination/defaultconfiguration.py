from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    """
    Default custom PageNumberPagination configuration
    """
    page_size = 10
