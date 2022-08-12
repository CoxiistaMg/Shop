from django.contrib import admin
from . import models


@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(models.SubCategoria)
class SubCategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Grupo)
class GruposAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Carrossel)
class CarroselAdmin(admin.ModelAdmin):
    pass

@admin.register(models.PesquisaTag)
class PesquisaTagAdmin(admin.ModelAdmin):
    pass