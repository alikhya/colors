from rest_framework.pagination import PageNumberPagination


class ColorPagination(PageNumberPagination):
    page_size = 5                      # default items per page
    page_size_query_param = "page_size"  # lets clients ask: ?page_size=10
    max_page_size = 100                # but never more than this