from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size=3

class MyPageNumberPaginationPinned(PageNumberPagination):
    page_size=1