from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    # 自定义分页器
    # 设置一页几条数据
    page_size = 5
    # 设置页码的参数，也就第几页
    page_query_param = 'page'
    # 设置每页数量的参数
    page_size_query_param = 'pagesize'
