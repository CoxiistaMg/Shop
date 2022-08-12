from django.db import models
from django.utils.text import slugify
from django.conf import settings
from stdimage import StdImageField
from uuid import uuid4


def filename(file, name):
    file = name.split('.')
    return f'produto/{uuid4()}.{file[-1]}'


class Categoria(models.Model):
    nome = models.CharField(max_length=40, unique=True)
    icon = models.CharField(max_length=20, choices=[('fas fa-gamepad', 'console'), ('fas fa-chess', 'jogos'),])
    descricao = models.TextField()
    slug = models.SlugField(editable=False)
    imagem = StdImageField()

    def __str__(self):
        return self.slug
    
    def save(self, **kwargs) -> None:
        self.slug = slugify(self.nome)
        return super().save(kwargs)


class PesquisaTag(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Grupo(models.Model):
    nome = models.CharField('Nome' ,unique=True, max_length=100)

    def __str__(self):
        return self.nome


class SubCategoria(models.Model):
    nome = models.CharField(max_length=60, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    icon = models.CharField(max_length=40, choices=[('fab fa-playstation', 'playstation'), ('fab fa-xbox', 'xbox'), ('fab fa-nintendo-switch', 'nintendo')])
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    imagem = StdImageField(upload_to=filename, variations={'thumb': (300, 300, True)})
    color = models.CharField(max_length=10, choices=[('primary','blue'), ('success', 'green'), ('danger', 'red')])

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100, unique=True)
    imagem = StdImageField('Imagem', upload_to=filename, variations={'thumb': (300, 300, False)})
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    quantidade = models.IntegerField('Quantidade')
    desconto = models.IntegerField('Desconto', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria')
    subcategoria = models.ForeignKey(to=SubCategoria, on_delete=models.CASCADE, related_name='subcategoria')
    pesquisa_tag= models.ManyToManyField(PesquisaTag, related_name='tags', blank=False)
    slug = models.SlugField(editable=False)
    informacao = models.TextField('Informações')
    descricao = models.TextField('Descrição')

    def save(self):
        self.slug = slugify(self.nome)
        super().save()
    
    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Produto'


class Carrinho(models.Model):
    dono = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(to=Produto, blank=True)

    def __str__(self):
        return f'{self.dono}|Carrinho'


class Carrossel(models.Model):
    categoria = models.ForeignKey(to=Categoria, on_delete=models.CASCADE)
    imagem = StdImageField(upload_to=filename)
    titulo = models.CharField(max_length=60)
    descricao = models.CharField(max_length=60)
    texto = models.TextField(max_length=1000)
    
    class Meta:
        verbose_name_plural = 'Carrossel'
        verbose_name = 'Carrossel'
    
    def save(self):
        self.slug = slugify(self.categoria.nome)
        return super().save()
    

