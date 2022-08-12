from django.template.defaultfilters import register
from shop.models import Produto, SubCategoria
import decimal
from account.models import Review


@register.filter(name='desconto')
def desconto(value, desconto):
    final = value - (decimal.Decimal(desconto)/ decimal.Decimal(100) * value)
    final = decimal.Decimal('{:.2f}'.format(final))
    return final


@register.filter(name='tamanho_do_carrinho')
def contador(session):
    try:
        carrinho = session['carrinho']
        if type(carrinho) != dict:
            session['carrinho'] = {}

        soma = 0
        for produto in carrinho:
            try:
                soma += carrinho[produto]
            except:
                del session['carrinho'][produto]

        
        return soma
        
    except KeyError:
        session['carrinho'] = {}
        session.modificad = True
    return 0
    

@register.filter(name='renderizar_carrinho')
def renderizar(session):
    carrinho = session['carrinho']
    render = []
    for produto in carrinho:
        try:
            query = Produto.objects.get(slug=produto)
            render.append(query)
        except Produto.DoesNotExist:
            del carrinho[query.slug]
            session.modificad = True

    return render
        

@register.filter(name='quantidade_produto')
def quant_produto(session, slug):
    carrinho = session['carrinho']
    return carrinho[slug]


@register.filter(name='soma')
def produto(session):
    carrinho = session['carrinho']
    soma = decimal.Decimal(0)
    
    for produto in carrinho:
        try: 
            prod = Produto.objects.get(slug=produto)

            value = prod.preco * decimal.Decimal(carrinho[produto])
            if prod.desconto:
                value -= (value *  decimal.Decimal(prod.desconto))
            soma += value 
        except:
            del carrinho[prod.slug]
            session.modificad = True
    
    soma = decimal.Decimal('{:.2f}'.format(soma))
    return soma


@register.filter
def nota(produto):
    reviews = Review.objects.filter(produto=produto.id)
    soma = 0
    for valor in reviews:
        soma += valor.nota 
    
    if len(reviews):
        return soma / len(reviews)
    return '0,0'


@register.filter
def quantidade(produto):
    reviews = Review.objects.filter(produto=produto.id)
    return len(reviews)


@register.filter
def categoria_sub(categoria):
    return SubCategoria.objects.filter(categoria=categoria)