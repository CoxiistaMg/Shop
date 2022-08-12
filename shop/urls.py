from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('produto/<slug:slug>', views.Produto.as_view(), name='produto'),
    path('add_kart/<slug:slug>/', views.adicionar_produto, name='add'),
    path('my_kart', views.meu_carrinho, name='carrinho'),
    path('remove_kart/<slug:slug>', views.remover_produto, name='remove'),
    path('comprar/', views.compra, name='finalizar_compra'),
    path('sobre/', views.ProjetoView.as_view(), name='sobre'),
    path('produto/<slug:slug>/review/avaliar', views.avaliar, name='avaliar'),
    path('produto/<slug:slug>/review/remover', views.remover_review, name='remover_review'),
    path('busca/', views.SearchList.as_view(), name='busca'),
    path('categoria/<slug:slug>', views.Categoria.as_view(), name='categoria')
]
