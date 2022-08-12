from django.views.generic import ListView, DetailView, TemplateView
from search_views.search import SearchListView
from django.shortcuts import redirect, render, get_object_or_404
from account.models import Review
from django.http import Http404
from django.urls import reverse_lazy
from . import models
from account.models import Review
from .search import ProdutoFilter

class Index(ListView):
    template_name = 'index.html'
    queryset = models.Produto.objects.all()
    paginate_by = 3

    def get_context_data(self):
        context = super().get_context_data()
        context['carrosel'] = models.Carrossel.objects.all()
        context['index'] = True
        context['menu'] = models.Categoria.objects.all()
        return context
    

class Produto(DetailView):
    template_name = 'produto.html'
    model = models.Produto
    
    def post(self, request, *args, **kwargs):
        return self.render_to_response({})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = context['object']
        if self.request.user.is_authenticated:
            context['avaliado'] = Review.objects.filter(usuario=self.request.user).filter(produto=object.id)
            context['review'] = Review.objects.filter(produto=object.id).exclude(usuario=self.request.user)
        
        else:
            context['review'] = Review.objects.filter(produto=object.id)
        informacao = object.informacao
        informacao = informacao.split('\n')
        context['informacao'] = informacao
        _id = object.subcategoria.id
        grupo = models.SubCategoria.objects.get(id=_id).grupo
        context['recomendados'] = models.SubCategoria.objects.filter(grupo=grupo).exclude(nome=object.subcategoria)
        return context


class ProjetoView(TemplateView):
    template_name = 'sobre.html'


class SearchList(SearchListView):
    model = models.Produto
    template_name = 'index.html'
    filter_class = ProdutoFilter

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context=context)

    
class Categoria(ListView):
    template_name = 'index.html'
    queryset = models.Produto.objects.all()
    

    def get_queryset(self):
        qy = super().get_queryset()
        if 'slug' in self.kwargs:
            self.categoria = get_object_or_404(models.Categoria, nome=self.kwargs['slug'].title())
            qy = qy.filter(categoria=self.categoria)
            return qy
    
    def get_context_data(self):
        context = super().get_context_data()
        context['carrosel'] = models.Carrossel.objects.filter(categoria=self.categoria)
        return context


def adicionar_produto(request, slug):
    if request.method == "POST":
        produto = get_object_or_404(models.Produto, slug=slug)

        try:
            qt = int(request.POST['quantidade'])
            request.session.modified = True
            if produto.quantidade > qt:
                print(qt, "----------")
                request.session['carrinho'][slug] = qt
                request.session.modified = True

            return redirect(reverse_lazy('carrinho'))
        
        except KeyError:
            pass
        
    
    raise Http404

def remover_produto(request, slug):
    carrinho = request.session['carrinho']
    if slug in carrinho:
        del carrinho[slug]
        request.session.modified = True
        return redirect(reverse_lazy('carrinho'))

    raise Http404

def meu_carrinho(request):
    context = {
    }
        
    return render(request, 'carrinho.html', context=context)

def compra(request):
    if request.user.is_anonymous:
        return redirect(reverse_lazy('login'))

    return render(request, 'finalizacao.html', {})

def avaliar(request, slug):
    if request.method == 'POST':
        if request.user.is_anonymous:
            return redirect(reverse_lazy('login'))
        
        try:
            nota = request.POST['ma']
            titulo = request.POST['titulo']
            descricao = request.POST['descricao']
            id_ = models.Produto.objects.get(slug=slug)

            Review.objects.create(nota=nota, titulo=titulo, comentario=descricao, usuario=request.user, produto=id_)
        
        except:
            pass 
        
        return redirect(reverse_lazy('produto', kwargs={'slug': slug}))

def remover_review(request, slug):
    if request.user.is_anonymous:
        return Http404()
    
    if request.method == "POST":
        id_ = models.Produto.objects.get(slug=slug)
        Review.objects.filter(produto=id_).filter(usuario=request.user).delete()

    return redirect(reverse_lazy('produto', kwargs={'slug': slug}))


