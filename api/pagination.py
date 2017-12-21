from rest_framework import pagination


class BranchListPagination(pagination.PageNumberPagination):
    page_size = 25
    page_query_param = 'page'