from search_views.filters import BaseFilter


class ProdutoFilter(BaseFilter):
    search_fields = {
        'search_text': ['nome']
    }